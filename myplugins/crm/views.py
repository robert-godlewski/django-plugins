from django.shortcuts import render
from django.http import HttpResponse
from .models import Task, Client, ClientTask


# Create your views here.
# For Tasks
def allTasks(request):
    # returns all of the tasks for the user
    # need to add in a user_id to only get those relative to the user
    print(request)
    #print(user_id)
    tasks = Task.objects.get()
    print(tasks)
    return HttpResponse(tasks)

def moveToPending(request):
    # moves the expired unfinished tasks to the pending list
    # will automatically set expired tasks is_pending = True
    print(request)
    return allTasks(request)

def allCurrentTasks(request):
    # returns a list of tasks that haven't past the due date
    print(request)
    #print(user_id)
    current = Task.objects.get(is_done=False, is_pending=False)
    print(current)
    return HttpResponse(current)

def allPendingTasks(request):
    # returns a list of tasks that have past the due date and need to be reschedualed
    print(request)
    #print(user_id)
    pending = Task.objects.get(is_pending=True)
    print(pending)
    return HttpResponse(pending)

def moveToFinished(request):
    # moves all tasks that are done to a different table
    # is_done = True will be set
    print(request)
    return allTasks(request)

def allDoneTasks(request):
    # returns a list of finished tasks
    print(request)
    #print(user_id)
    finished = Task.objects.get(is_done=True)
    print(finished)
    return HttpResponse(finished)

def oneTask(request, id):
    # get the details for one task
    print(request)
    print(id)
    task = Task.objects.get(id=id)
    print(task)
    return HttpResponse(task)

def createTask(request):
    print(request)
    return allTasks(request)

def updateTask(request, id):
    print(request)
    print(id)
    return allTasks(request)

def destroyTask(request, id):
    print(request)
    print(id)
    return allTasks(request)

# For Clients
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

def createClient(request):
    print(request)
    return allClients(request)

def updateClient(request, id):
    print(request)
    print(id)
    return allClients(request)

# For clients and tasks
def createClientTaskRelation(request, client, task):
    print(request)
    print(client)
    print(task)
    return allTasks(request)
