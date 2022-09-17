from django.contrib import admin
from .models import Task, Client, ClientTask


# Register your models here.
admin.site.register(Task)
admin.site.register(Client)
admin.site.register(ClientTask)
