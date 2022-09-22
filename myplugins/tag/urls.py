from django.urls import path
from . import views


urlpatterns = [
    path('', views.allTags),
    path('create_tag/', views.createTag),
    path('<str:name>/', views.oneTag),
    #path('update_tag/<str:name>/', views.updateTag),
    #path('delete_tag/<str:name>/', views.deleteTag),
]
