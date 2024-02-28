from datetime import timedelta
#, datetime, tzinfo

from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from .forms import PostForm, CommentForm
from .models import Post, Comment, Profile, Tag


# All published posts and draft posts for the logged in user
def allblogs(request):
    tags = Tag.objects.all()
    # Need to update all of the posts here for publishing
    end = timezone.datetime.now()
    start = end - timedelta(days=2)
    unpub_posts = Post.objects.filter(published=False, publish_date__range=(start, end))
    for dp in unpub_posts:
        dp.published = True
        dp.save()
    # All posts
    featured = Post.objects.filter(featured=True, published=True)
    posts = Post.objects.filter(published=True)
    posts.order_by('-publish_date')#[0:3]
    # Take out all of the draft_posts and pub_posts from here to the user's detail page instead
    #print(request.user)
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
        draft_posts = Post.objects.filter(author=profile, published=False)
        # Posts where the author = current user
        pub_posts = Post.objects.filter(author=profile, published=True)
        pub_posts.order_by('-publish_date')
    else:
        user = None
        draft_posts = None
        pub_posts = None
    context = {
        'user': user,
        'featured': featured,
        'posts': posts,
        'tags': tags,
        'drafts': draft_posts,
        'pub_posts': pub_posts
    }
    return render(request, 'blog/index.html', context)

# Single post routes
def one_post(request, slug):
    post = Post.objects.get(slug=slug)
    if request.user.is_authenticated:
        author = Profile.objects.get(user=request.user)
    else:
        author = None
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'author': author,
        'comments': comments
    }
    return render(request, template_name='blog/onepost.html', context=context)

def create_post(request):
    if not request.user.is_authenticated:
        return redirect('/logout')
    # Might need to add the is_staff and is_superuser conditions to other routes when needed but looks like it works right now
    #print(f"Is @{request.user.username} a staff member? {request.user.is_staff}")
    #print(f"Is @{request.user.username} a superuser? {request.user.is_superuser}")
    if not request.user.is_staff:
        # and not request.user.is_superuser:
        return redirect('/blog/post/all')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Need to grab the user for the author
            user = User.objects.get(username=request.user)
            author = Profile.objects.get(user=user)
            # Need to create the slug from the title and subtitle
            title = form.cleaned_data['title']
            subtitle = form.cleaned_data['subtitle']
            slug = slugify(title)
            if subtitle:
                slug += '-' + slugify(subtitle)
            content = form.cleaned_data['content']
            featured = form.cleaned_data['featured']
            publish_date = form.cleaned_data['publish_date']
            post = Post(
                title=title,
                subtitle=subtitle,
                slug=slug,
                content=content,
                featured=featured,
                publish_date=publish_date,
                author=author
            )
            try:
                post.save()
                messages.success(request, 'Created new post.')
            except:
                messages.error(request, 'Did not save the new post.')
            #print(f'post = {post}')
            return redirect(f'/blog/post/read/{post.slug}')
        messages.error(request, "Did not save the new post.")
    else: 
        form = PostForm()
    return render(request, template_name='blog/createpost.html', context={'form': form})

# Provides the form to update the form for later
def edit_post(request, slug):
    if not request.user.is_authenticated:
        return redirect('/logout')
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
        'form': PostForm(instance=post)
    }
    return render(request, template_name='blog/editpost.html', context=context)

# Either saves the updates or redirects back to the editing form
def update_post(request, slug):
    if not request.user.is_authenticated:
        return redirect('/logout')
    post = Post.objects.get(slug=slug)
    form = PostForm(data=request.POST, instance=post)
    if form.is_valid():
        form.save()
        return redirect(f'/blog/post/read/{post.slug}')
    context = {
        'post': post,
        'form': PostForm(instance=post)
    }
    return render(request, template_name='blog/editpost.html', context=context)

# Asks the user if they actually want to delete one of their posts or not
def delete_post(request, slug):
    if not request.user.is_authenticated:
        return redirect('/logout')
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render(request, template_name='blog/deletepost.html', context=context)

# Actually removes the post from the database
def destroy_post(request, slug):
    if not request.user.is_authenticated:
        return redirect('/user/logout')
    post = Post.objects.get(slug=slug)
    post.delete()
    return redirect('/')

def create_comment(request, post_slug):
    if not request.user.is_authenticated:
        return redirect('/logout')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user)
            author = Profile.objects.get(user=user)
            post = Post.objects.get(slug=post_slug)
            content = form.cleaned_data['content']
            comment = Comment(
                author=author,
                post=post,
                content=content
            )
            try:
                comment.save()
                messages.success(request, 'Created new comment.')
            except:
                messages.error(request, 'Did not save the new comment.')
            print(f'comment = {comment}')
            return redirect(f'/blog/post/read/{post_slug}')
        messages.error('Invalid information to make a comment.')
    else:
        form = CommentForm()
    context = {
        'form': form,
        'post_slug': post_slug
    }
    return render(request, template_name='blog/createcomment.html', context=context)

def edit_comment(request, post_slug, comment_id):
    if not request.user.is_authenticated:
        return redirect('/logout')
    comment = Comment.objects.get(pk=comment_id)
    print(comment.id)
    form = CommentForm(instance=comment)
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    print(user.username)
    context = {
        'profile': profile,
        'comment': comment,
        'form': form,
        'post_slug': post_slug
    }
    return render(request, template_name='blog/editcomment.html', context=context)

def update_comment(request, post_slug, comment_id):
    if not request.user.is_authenticated:
        return redirect('/logout')
    comment = Comment.objects.get(pk=comment_id)
    form = CommentForm(data=request.POST, instance=comment)
    if form.is_valid():
        form.save()
        return redirect(f'/blog/post/read/{post_slug}')
    form = CommentForm(instance=comment)
    context = {
        'comment': comment,
        'form': form,
        'post_slug': post_slug
    }
    return render(request, 'blog/editcomment.html', context=context)

def delete_comment(request, post_slug, comment_id):
    if not request.user.is_authenticated:
        return redirect('/logout')
    comment = Comment.objects.get(pk=comment_id)
    post = Post.objects.get(slug=post_slug)
    context = {
        'comment': comment,
        'post': post
    }
    return render(request, template_name='blog/deletecomment.html', context=context)

def destroy_comment(request, post_slug, comment_id):
    if not request.user.is_authenticated:
        return redirect('/logout')
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect(f'/blog/post/read/{post_slug}/')