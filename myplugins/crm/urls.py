from django.urls import path
from . import views


urlpatterns =[
    path('', views.crmdash),
    # Task views
    path('task/all/', views.allTasks),
    path('task/create/', views.createTask),
    path('task/one_task/<int:id>/', views.oneTask)
    # Need to create a special view for just tasks of current, pending, past, etc.
    #path('task/<int:id>/', views.oneTask),
    #path('client/', views.allClients),
    #path('client/<email:email>', views.oneClient)
]
