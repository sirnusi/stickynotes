from django.db import models
from django.contrib.auth.admin import User
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.name


class Notes(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

    class Meta():
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
