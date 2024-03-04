from django.db import models
from django.contrib.auth.models import User


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
