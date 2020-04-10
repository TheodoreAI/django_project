from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Add your models here.

class Profile(models.Model):
    """ Adding the fields for the user's Models"""

    # if the user is deleted CASCADE deletes everything from the user field
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # image fields, this is where we could add the fields for the user to add their products to sale
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # # products
    # product = models.ImageField()
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kawrgs):
        """ This method is used to resize the uploaded images """
        super().save(*args, **kawrgs)

        # this object will resize the photos/ could be done with a template that makes it more efficient
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)
