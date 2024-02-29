from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# from django.conf import settings
# from appname.models import Profile, Tag


# For any users who sign up to be subscribed to the blog - migrate to other plugins when needed
# class Profile(models.Model):
#     # More details of the user profile to use this to expand on: https://docs.djangoproject.com/en/4.1/ref/contrib/auth/
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )
#     website = models.URLField(blank=True)
#     bio = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self) -> str:
#         return self.user.get_username()


# Searchable items for SEO purposes - migrate to other plugins when needed
# class Tag(models.Model):
#     name = models.CharField(max_length=30, unique=True, blank=False)

#     def __str__(self) -> str:
#         return self.name


# Grouping for the blogs
class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.title


# Actual blog post
class Post(models.Model):
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

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # tags = models.ManyToManyField(Tag, blank=True)

    class Meta: ordering = ["-publish_date"]

    def __str__(self) -> str:
        return self.title


# Adding a way to implement comments
class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta: ordering = ["-created_at"]
