from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Task
from .forms import TaskForm


# Create your views here.
# crm dashboard
def crmdash(request):
    print(request)
    # Change tasks to only get the current/ future ones not pending and unfinished
    tasks = Task.objects.all()
    print(tasks)
    context = {
        'tasks': tasks
    }
    #return HttpResponse("CRM Dashboard")
    return render(request, template_name='crm/crmdash.html', context=context)

# For Tasks
def allTasks(request):
    #print(request)
    tasks = Task.objects.all()
    #print(tasks)
    context = {
        # Split up the tasks later
        'tasks': tasks
    }
    #return HttpResponse("CRM Dashboard")
    return render(request, template_name='crm/allTasks.html', context=context)

def createTask(request):
    #print(request)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/crm/task/all')
    else:
        form = TaskForm()
    return render(request, template_name='crm/createTask.html', context={'form': form})

def oneTask(request, id):
    # get the details for one task
    #print(request)
    #print(id)
    task = Task.objects.get(id=id)
    #print(task)
    return render(request, template_name='crm/oneTask.html', context={'task': task})

def updateTask(request, id):
    #print(request)
    #print(id)
    task = Task.objects.get(id=id)
    #print(task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/crm/task/one_task/{id}')
    else:
        form = TaskForm(instance=task)
    context = {
        "task": task,
        "form": form
    }
    return render(request, template_name='crm/updateTask.html', context=context)

def deleteTask(request, id):
    print(request)
    print(id)
    task = Task.objects.get(id=id)
    print(task)
    if request.method == "POST":
        print(f"deleting {task}")
        task.delete()
        return HttpResponseRedirect('/crm/task/all')
    return render(request, template_name='crm/deleteTask.html', context={'task': task})

# For deleting
'''
def deleteTag(request, name):
    print(request)
    print(name)
    tag = Tag.objects.get(name=name)
    print(tag)
    if request.method == "POST":
        print(f"deleting {tag}")
        tag.delete()
        return HttpResponseRedirect('/tag')
    return render(request, template_name='tag/deleteTag.html', context={'tag': tag})
'''

'''
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
'''
