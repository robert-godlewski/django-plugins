from django.urls import path
from . import views


urlpatterns =[
    path('task/', views.allTasks),
    path('task/<int:id>/', views.oneTask),
    path('client/', views.allClients),
    path('client/<email:email>', views.oneClient)
]
