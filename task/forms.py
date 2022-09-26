from django import forms
from .models import Tasks
class Taskform(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder':'Escriba su tarea'}),
            'description': forms.Textarea(attrs={ 'class': 'form-control', 'placeholder':'Escriba su tarea'}),
            'important': forms.CheckboxInput(attrs={ 'class': 'form-check-input text-center'}),
            
        }