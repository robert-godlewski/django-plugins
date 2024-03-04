from django import forms

from .models import Category, Post, Comment


class PostForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=True)
    title = forms.CharField(label="Title", min_length=1, max_length=255)
    subtitle = forms.CharField(label="Subtitle (optional)", min_length=1, max_length=255, required=False)
    content = forms.Textarea()
    featured = forms.BooleanField(label="Want to feature this post?", required=False)
    comments_disabled = forms.BooleanField(label="Do you want to disable comments?", required=False)
    hide_details = forms.BooleanField(label="Hide the details of this post from the public?", required=False)
    publish_date = forms.DateTimeField(label="Date you want to publish this", widget=forms.SelectDateWidget(), required=False)

    class Meta:
        model = Post
        fields = [
            'category',
            'title',
            'subtitle',
            'content',
            'featured',
            'publish_date',
        ]


class CommentForm(forms.ModelForm):
    name = forms.CharField(label="Your Name", min_length=2, max_length=255)
    email = forms.EmailField(label="Your Email")
    content = forms.Textarea()

    class Meta:
        model = Comment
        fields = ['name','email','content']
