from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=150)
    image = models.ImageField(default='default.jpg', upload_to='project_pics')
    link = models.CharField(max_length=100, default="#")


class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=100)
    content = models.TextField(max_length=300)