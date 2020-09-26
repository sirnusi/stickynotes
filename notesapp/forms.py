from django import forms
from .models import Notes


class NoteForm(forms.ModelForm):
    class Meta():
        model = Notes
        fields = ['title', 'category', 'due_date']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John Doe'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }
