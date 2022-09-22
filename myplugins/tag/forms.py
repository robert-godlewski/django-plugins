# Used to create new tags
from django import forms
from .models import Tag


class TagForm(forms.ModelForm):
    name = forms.CharField(label="tag name", min_length=1, max_length=50)

    class Meta:
        model = Tag
        fields = ['name']
