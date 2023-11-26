from django import forms
from .models import *


class InputTaskForm(forms.ModelForm):
    task = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter a task here", "label": ''}), label='')

    class Meta:
        model = Task
        fields = ('task', )