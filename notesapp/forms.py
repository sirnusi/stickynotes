from django import forms
from .models import Notes


class NoteForm(forms.ModelForm):
    class Meta():
        model = Notes
        fields = ['title', 'category', 'due_date']

        widgets = {
            'title': forms.TextInput(attrs={'label': 'Title:', 'class': 'form-control', 'placeholder': 'What you want to do!'}),
            'category': forms.Select(attrs={'label': 'Category:', 'class': 'form-control'}),

        }
