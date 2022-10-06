from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe un título'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe una descripción'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'})
        }