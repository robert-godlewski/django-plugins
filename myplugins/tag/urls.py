from django.urls import path
from . import views


urlpatterns = [
    path('', views.allTags),
    path('one_tag/<str:name>/', views.oneTag),
    path('create_tag/', views.createTag),
    path('delete_tag/<str:name>/', views.deleteTag),
]
