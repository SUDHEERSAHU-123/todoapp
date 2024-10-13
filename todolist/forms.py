from django import forms
from .models import Todolist

class TodoListForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['text']
