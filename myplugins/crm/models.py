from django.db import models
from django.conf import settings


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(blank=True)
    TOP_P = 'TOP'
    #HIGH_P = 'H'
    MID_P = 'MID'
    LOW_P = 'LOW'
    # Change the choices to match above
    PRIORITY_CHOICES = [
        (TOP_P, 'top'),
        (MID_P, 'mid'),
        (LOW_P, 'low')
    ]
    priority = models.CharField(
        max_length=3,
        choices=PRIORITY_CHOICES,
        default=TOP_P
        #default=HIGH_P
    )
    is_recurring = models.BooleanField(default=False)
    reminder = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now=True)
    # By default will be in a list of current tasks
    # This will move the task to a finished group if true
    is_done = models.BooleanField(default=False)
    # This will move the task to a group of unfinished group of tasks not finished past the due date that needs to be finished 
    is_pending = models.BooleanField(default=False)
    # Mainly for login information about a specific user
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True)

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    f_name = models.CharField(max_length=100)
    m_name = models.CharField(max_length=100, blank=True)
    l_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    notes = models.TextField(blank=True)
    # Mainly for login information about a specific user
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.full_name()

    def full_name(self) -> str:
        if self.m_name:
            return f"{self.f_name} {self.m_name} {self.l_name}"
        else:
            return f"{self.f_name} {self.l_name}"


class ContactTask(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
