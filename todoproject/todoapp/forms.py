from dataclasses import fields
from xml.parsers.expat import model
from . models import Task
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']