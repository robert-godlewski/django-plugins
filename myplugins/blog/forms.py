from django import forms
# auth is only needed for UserForm and ProfileForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import Post, Comment, Profile, Tag


# Temporarily have both UserForm and ProfileForm here until we have the registration app
class UserForm(UserCreationForm):
    username = forms.CharField(label='User Name (cannot edit later!):', required=True, max_length=191, min_length=2)
    first_name = forms.CharField(label='First Name:', required=False)
    last_name = forms.CharField(label='Last Name:', required=False)
    email = forms.EmailField(label='Email Address:', required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        # print(user)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit: 
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    website = forms.URLField(label='Website URL:', required=False)
    bio = forms.Textarea()

    class Meta:
        model = Profile
        fields = ['website', 'bio']

    def save(self, username, commit=True):
        user = User.objects.get(username=username)
        # print(user)
        profile = super(ProfileForm, self).save(commit=False)
        profile.user = user
        profile.website = self.cleaned_data['website']
        profile.bio = self.cleaned_data['bio']
        if commit: 
            profile.save()
        return profile


# Temporarily have this for Tag until we have the tag app operational with Docker
class TagForm(forms.ModelForm):
    name = forms.CharField(label="tag name", min_length=1, max_length=50)

    class Meta:
        model = Tag
        fields = ['name']


# Necessary classes for the blog stay here
class PostForm(forms.ModelForm):
    title = forms.CharField(label="Title", min_length=1, max_length=255)
    subtitle = forms.CharField(label="Subtitle (optional)", min_length=1, max_length=255, required=False)
    content = forms.Textarea()
    featured = forms.BooleanField(label="Want to feature this post?", required=False)
    comments_disabled = forms.BooleanField(label="Do you want to disable comments?", required=False)
    hide_details = forms.BooleanField(label="Hide the details of this post from the public?", required=False)
    publish_date = forms.DateTimeField(label="Date you want to publish this", widget=forms.SelectDateWidget(), required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)

    class Meta:
        model = Post
        fields = [
            'title',
            'subtitle',
            'content',
            'featured',
            'publish_date',
            'tags',
        ]


class CommentForm(forms.ModelForm):
    content = forms.Textarea()

    class Meta:
        model = Comment
        fields = ['content']
