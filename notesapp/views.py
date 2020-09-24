from django.shortcuts import render
from django.views.generic import ListView
from .models import Notes
# Create your views here.


class ListNotes(ListView):
    template_name = 'notesapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Notes.objects.all()
        return context
