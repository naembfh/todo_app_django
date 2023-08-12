from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields =['taskTitle','taskDescription']
        widgets = {
            'taskTitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task Title'}),
            'taskDescription': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Task Description', 'rows': 4}),
        }
        labels = {
            'taskTitle': 'Task Title',
            'taskDescription': 'Task Description',
        }