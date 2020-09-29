from django import forms
from .models import Notes
from django.contrib.auth.admin import User
from django.contrib.auth.forms import UserCreationForm


class NoteForm(forms.ModelForm):
    class Meta():
        model = Notes
        fields = ['title', 'category', 'due_date']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John Doe'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }


class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
