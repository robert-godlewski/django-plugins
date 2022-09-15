from django.shortcuts import render
from django.http import HttpResponse
from .models import Task, Client, ClientTask


# Create your views here.
def allTasks(request):
    # need to add in a user_id to only get those relative to the user
    print(request)
    #print(user_id)
    tasks = Task.objects.get()
    print(tasks)
    return HttpResponse(tasks)

def oneTask(request, id):
    print(request)
    print(id)
    task = Task.objects.get(id=id)
    print(task)
    return HttpResponse(task)

def allClients(request):
    # need to add in a user_id to only get those relative to the user
    print(request)
    #print(user_id)
    clients = Client.objects.get()
    print(clients)
    return HttpResponse(clients)

def oneClient(request, email):
    print(request)
    print(email)
    client = Client.objects.get(email=email)
    print(client)
    return HttpResponse(client)
