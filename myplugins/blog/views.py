from datetime import timedelta
#, datetime, tzinfo

from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from .forms import PostForm, CommentForm
from .models import Category, Post, Comment


# All published posts and draft posts for the logged in user
def allblogs(request):
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
    categories = Category.objects.all()
    # Take out all of the draft_posts and pub_posts from here to the user's detail page instead
    #print(request.user)
    if request.user.is_authenticated:
        user = request.user
        draft_posts = Post.objects.filter(author=user, published=False)
        # Posts where the author = current user
        pub_posts = Post.objects.filter(author=user, published=True)
        pub_posts.order_by('-publish_date')
    else:
        user = None
        draft_posts = []
        pub_posts = []
    context = {
        'user': user,
        'featured': featured,
        'posts': posts,
        'drafts': draft_posts,
        'pub_posts': pub_posts,
        'categories': categories,
        'category_id': None
    }
    return render(request, 'blog/index.html', context)

# Grabs all posts from the given id of a category
def posts_by_category(request, id):
    # Need to update all of the posts here for publishing
    end = timezone.datetime.now()
    start = end - timedelta(days=2)
    unpub_posts = Post.objects.filter(published=False, publish_date__range=(start, end))
    for dp in unpub_posts:
        dp.published = True
        dp.save()
    category = Category.objects.filter(id=id)
    featured = Post.objects.filter(featured=True, published=True, category=id)
    posts = Post.objects.filter(published=True, category=id)
    posts.order_by('-publish_date')#[0:3]
    categories = Category.objects.all()
    # Take out all of the draft_posts and pub_posts from here to the user's detail page instead
    #print(request.user)
    if request.user.is_authenticated:
        user = request.user
        draft_posts = Post.objects.filter(author=user, published=False)
        # Posts where the author = current user
        pub_posts = Post.objects.filter(author=user, published=True)
        pub_posts.order_by('-publish_date')
    else:
        user = None
        draft_posts = []
        pub_posts = []
    context = {
        'user': user,
        'featured': featured,
        'posts': posts,
        'drafts': draft_posts,
        'pub_posts': pub_posts,
        'categories': categories,
        'category_id': id
    }
    return render(request, 'blog/index.html', context)

# Single post routes
def one_post(request, slug):
    post = Post.objects.get(slug=slug)
    # This is for creating a comment
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                user = User.objects.get(username=request.user.username)
                name = user.get_full_name()
                email = user.email
            else:
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            comment = Comment(name=name,email=email,content=content,post=post)
            try:
                comment.save()
                form = CommentForm()
                messages.success(request,'Created new comment.')
            except:
                messages.error(request, 'Did not save the new comment.')
    else:
        form = CommentForm()
    # Getting the other data
    if request.user.is_authenticated:
        author = User.objects.get(username=request.user.username)
    else:
        author = None
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'author': author,
        'comments': comments,
        'form': form
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
            author = User.objects.get(username=request.user)
            # Need to create the slug from the title and subtitle
            title = form.cleaned_data['title']
            subtitle = form.cleaned_data['subtitle']
            slug = slugify(title)
            if subtitle:
                slug += '-' + slugify(subtitle)
            content = form.cleaned_data['content']
            featured = form.cleaned_data['featured']
            publish_date = form.cleaned_data['publish_date']
            category = form.cleaned_data['category']
            post = Post(
                title=title,
                subtitle=subtitle,
                slug=slug,
                content=content,
                featured=featured,
                publish_date=publish_date,
                category=category,
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
    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated post.')
        return redirect(f'/blog/post/read/{post.slug}')
    except:
        messages.error(request, 'Not able to update the post')
        print(form)
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
