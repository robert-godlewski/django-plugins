from django.urls import path
from . import views


urlpatterns =[
    path('', views.crmdash),
    # Task views
    path('task/all/', views.allTasks),
    path('task/create/', views.createTask),
    path('task/one_task/<int:id>/', views.oneTask),
    path('task/update/<int:id>', views.updateTask),
    path('task/delete/<int:id>', views.deleteTask),
    # Need to create a special view for just tasks of current, pending, past, etc for tasks.
    # Also need to add in the other views.
]
