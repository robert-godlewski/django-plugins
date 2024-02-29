from django.urls import path
from . import views

comment_base = 'post/read/<str:post_slug>'

urlpatterns = [
    # urls that need to stay
    # For Posts
    path('post/all/', views.allblogs, name='blogs'),
    path('post/new/', views.create_post, name='newpost'),
    path('post/read/<str:slug>/', views.one_post, name='onepost'),
    path('post/edit/<str:slug>/', views.edit_post, name='editpost'),
    path('post/update/<str:slug>/', views.update_post, name='updatepost'),
    path('post/delete/<str:slug>/', views.delete_post, name='deletepost'),
    path('post/destroy/<str:slug>/', views.destroy_post, name='destroypost'),
    # For Comments
    path(f'{comment_base}/comment/new/', views.create_comment, name='createcomment'),
    path(f'{comment_base}/comment/edit/<int:comment_id>/', views.edit_comment, name='editcomment'),
    path(f'{comment_base}/comment/update/<int:comment_id>/', views.update_comment, name='updatecomment'),
    path(f'{comment_base}/comment/delete/<int:comment_id>/', views.delete_comment, name='deletecomment'),
    path(f'{comment_base}/comment/destroy/<int:comment_id>/', views.destroy_comment, name='destroycomment')
]
