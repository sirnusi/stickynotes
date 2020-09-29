from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.forms import UserCreationForm
from .models import Notes, Category
from .forms import NoteForm, UserRegister
# Create your views here.


class ListNotes(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'notesapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Notes.objects.filter(author=self.request.user)
        return context


class CreateNote(LoginRequiredMixin, CreateView):
    model = Notes
    form_class = NoteForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CreateCategory(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name', ]


class DeleteNote(DeleteView):
    model = Notes
    success_url = reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = UserRegister
    template_name = 'notesapp/signup.html'
    success_url = reverse_lazy('login')
