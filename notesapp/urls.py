from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListNotes.as_view(), name='home')
]
