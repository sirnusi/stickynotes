from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('newcategory/', views.CreateCategory.as_view(), name='new_category'),
    path('<int:pk>/delete/', views.DeleteNote.as_view(), name='delete_note'),
    path('new/', views.CreateNote.as_view(), name='new_note'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='notesapp/login.html'), name='login'),
    path('', views.ListNotes.as_view(), name='home')
]
