from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(label="task title", min_length=2, max_length=50)
    body = forms.CharField(label="body", required=False)
    # Multiple choice area
    '''
    HIGH_P = 'H'
    MID_P = 'M'
    LOW_P = 'L'
    PRIORITY_CHOICES = [
        (HIGH_P, 'high'),
        (MID_P, 'mid'),
        (LOW_P, 'low')
    ]
    priority = forms.CharField(
        label="priority",
        max_length=1,
        choices=PRIORITY_CHOICES,
        default=HIGH_P
    )
    '''
    #is_recurring = forms.BooleanField(label="recurring", default=False)
    #reminder = models.DateTimeField(auto_now_add=True)
    #due_date = models.DateTimeField(auto_now=True)
    # By default will be in a list of current tasks
    # This will move the task to a finished group if true
    #is_done = models.BooleanField(default=False)
    # This will move the task to a group of unfinished group of tasks not finished past the due date that needs to be finished 
    #is_pending = models.BooleanField(default=False)

    class Meta:
        model = Task
        fields = ['title','body']
        widgets = {
            'body': forms.Textarea(attrs={'cols': 80, 'rows': 20})
        }
