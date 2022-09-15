from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(blank=True)
    HIGH_P = 'H'
    MID_P = 'M'
    LOW_P = 'L'
    PRIORITY_CHOICES = [
        (HIGH_P, 'high'),
        (MID_P, 'mid'),
        (LOW_P, 'low')
    ]
    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default=HIGH_P
    )
    is_recurring = models.BooleanField(default=False)
    reminder = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
    #user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title


class Client(models.Model):
    f_name = models.CharField(max_length=100)
    m_name = models.CharField(max_length=100, blank=True)
    l_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    #user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.full_name()

    def full_name(self) -> str:
        if self.m_name:
            return f"{self.f_name} {self.m_name} {self.l_name}"
        else:
            return f"{self.f_name} {self.l_name}"


class ClientTask(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
