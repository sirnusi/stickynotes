from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notes
from .forms import NoteForm
# Create your views here.


class ListNotes(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'notesapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Notes.objects.filter(author=self.request.user)
        return context


class CreateNote(CreateView):
    model = Notes
    form_class = NoteForm
