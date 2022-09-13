from django.urls import path
from . import views


urlpatterns = [
    path('', views.allTags),
    path('<str:name>/', views.oneTag),
]
