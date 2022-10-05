from django import forms
from .models import Task


# Group of Choices
PRIORITY_CHOICES = [
    ('TOP', 'top'),
    ('MID', 'mid'),
    ('LOW', 'low')
]


class TaskForm(forms.ModelForm):
    title = forms.CharField(label="task title", min_length=2, max_length=50)
    body = forms.CharField(
        label="body", 
        required=False
    )
    priority = forms.CharField(
        label="priority",
        required=True,
        widget=forms.Select(choices=PRIORITY_CHOICES)
    )
    is_recurring = forms.BooleanField(
        label="recurring", 
        required=False,
        widget=forms.CheckboxInput()
    )
    #reminder = forms.DateTimeField(label="reminder", auto_now_add=True)
    #due_date = models.DateTimeField(auto_now=True)
    # By default will be in a list of current tasks
    # This will move the task to a finished group if true
    #is_done = models.BooleanField(default=False)
    # This will move the task to a group of unfinished group of tasks not finished past the due date that needs to be finished 
    #is_pending = models.BooleanField(default=False)

    class Meta:
        model = Task
        fields = ['title','body','priority']
        widgets = {
            'body': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
