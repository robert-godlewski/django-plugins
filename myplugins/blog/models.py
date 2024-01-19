from django.db import models
# from django.contrib.auth import get_user_model
from django.conf import settings
# from appname.models import Profile, Tag


# For any users who sign up to be subscribed to the blog - migrate to other plugins when needed
class Profile(models.Model):
    # More details of the user profile to use this to expand on: https://docs.djangoproject.com/en/4.1/ref/contrib/auth/
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    website = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.get_username()


# Searchable items for SEO purposes - migrate to other plugins when needed
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)

    def __str__(self) -> str:
        return self.name


# Actual blog post
class Post(models.Model):
    class Meta: ordering = ["-publish_date"]

    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(null=False, unique=True)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    comments_disabled = models.BooleanField(default=False)
    hide_details = models.BooleanField(default=False)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self) -> str:
        return self.title


# Adding a way to implement comments
class Comment(models.Model):
    class Meta: ordering = ["-created_at"]

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
