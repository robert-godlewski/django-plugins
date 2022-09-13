from django.shortcuts import render
from django.http import HttpResponse
from .models import Tag


# Create your views here.
def allTags(request):
    print(request)
    tags = Tag.objects.get()
    print(tags)
    return HttpResponse(tags)

def oneTag(request, name):
    print(request)
    #print(name)
    tag = Tag.objects.get(name=name)
    print(tag)
    return HttpResponse(tag)
