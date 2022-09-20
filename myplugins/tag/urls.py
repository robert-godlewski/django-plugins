from django.urls import path
from . import views


urlpatterns = [
    path('', views.allTags),
    path('<str:name>/', views.oneTag),
    path('create_tag/', views.createTag),
    path('update_tag/<str:name>/', views.updateTag),
    path('delete_tag/<str:name>/', views.deleteTag),
]
