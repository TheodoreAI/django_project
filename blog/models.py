from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Post(models.Model):

    # field of post table; has a restriction of 100 characters
    title = models.CharField(max_length=100)
    # unrestricted test field for how long they wanna make it
    content = models.TextField()
    # when the post was created passing the function (now without the parenetheses) as default value
    date_posted = models.DateTimeField(default=timezone.now)    

    # another one for the author to delete the user's content when their account is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        """Special method that returns the title of the post"""
        return self.title

    def get_absolute_url(self):
        """This reverses the url so that a post gets done correctly """
        return reverse("post-detail", kwargs={"pk": self.pk})
    