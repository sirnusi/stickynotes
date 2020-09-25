from django import forms
from .models import Notes


class NoteForm(forms.ModelForm):
    due_date = forms.DateField(
        label='Due date for the task', widget=forms.SelectDateWidget)

    class Meta():
        model = Notes
        fields = ['title', 'category', 'due_date']
