from todolist.models import Tasktodolist
from django import forms
from django.forms import ModelForm

class taskform(ModelForm):
    title = forms.CharField(
        required=True
    ) 
    description = forms.Textarea(
    )
    
    class Meta:
        model = Tasktodolist
        fields = ('user', 'date', 'title', 'description')
        exclude = ['user', 'date']