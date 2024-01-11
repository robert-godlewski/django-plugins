from django.shortcuts import render, redirect


def index(request):
    # For now just have the whole side reference the admin
    return redirect('/admin/login/')
