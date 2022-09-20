# Used to create new tags
from django import forms
from .models import Tag


class TagForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "name"
    }))

    class Meta:
        model = Tag
        fields = ['name']
