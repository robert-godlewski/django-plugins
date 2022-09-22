from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
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
    #print(request)
    if request.method == "POST":
        form = TagForm(request.POST)
        #print(form)
        # The form will be checked by the model if the name is unique or not
        if form.is_valid():
            # This will automatically save it to the db
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TagForm()
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
