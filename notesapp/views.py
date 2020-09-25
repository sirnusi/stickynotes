from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notes
from .forms import NoteForm
# Create your views here.


class ListNotes(CreateView):
    model = Notes
    template_name = 'notesapp/home.html'
    form_class = NoteForm

    def form_valid(self, form):
        author_id = self.kwargs.get('author_id')
        notes = get_object_or_404(Notes, id=author_id)
        self.success_url = f'/notes/'
        form.instance.notes = notes
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Notes.objects.all()
        return context
