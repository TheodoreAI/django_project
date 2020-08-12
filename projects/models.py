from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse


# Create your models here.
class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=150)
    image = models.ImageField(default='default.jpg', upload_to='project_pics')
    link = models.CharField(max_length=100, default=" ")
    date_posted = models.DateTimeField(default=datetime.now, blank=True)
    github = models.CharField(max_length=100, default=" ")


    def __str__(self):
        """Special method that returns the title of the post"""
        return self.title

    def get_absolute_url(self):
        """This reverses the url so that a post gets done correctly """
        return reverse("project-detail", kwargs={"pk": self.pk})


class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=100)
    content = models.TextField(max_length=300)