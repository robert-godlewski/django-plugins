from django.shortcuts import render, redirect, get_object_or_404
#from django.http import HttpResponse
from .models import Tag
from .forms import TagForm


# Create your views here.
def allTags(request):
    #print(request)
    tags = Tag.objects.all()
    #print(tags)
    #return HttpResponse(tags)
    return render(request, template_name='tag/allTags.html', context={'tags': tags})

def oneTag(request, name):
    #print(request)
    #print(name)
    tag = Tag.objects.get(name=name)
    #print(tag)
    #return HttpResponse(tag)
    return render(request, template_name='tag/oneTag.html', context={'tag': tag})

def createTag(request):
    # This is a post request here
    print(request)
    form = TagForm(request.POST or None)
    print(request.method)
    if request.method == "POST":
        if form.is_valid():
            Tag.objects.create(name=form.name)
            return redirect(oneTag(request, form.name))
    return render(request, template_name='tag/createTag.html', context={'form': form})

def updateTag(request, name):
    print(request)
    print(name)
    tag = Tag.objects.get(name=name)
    print(tag)
    return oneTag(request, name)

def deleteTag(request, name):
    print(request)
    print(name)
    tag = Tag.objects.get(name=name)
    print(tag)
    return allTags(request)
