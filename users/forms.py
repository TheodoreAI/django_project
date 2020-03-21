from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# User registration form to create the User's


class UserRegisterForm(UserCreationForm):
    # required email since the default is True for the parameter in EmailField()
    email = forms.EmailField()

    class Meta:
        model = User
        # this will be the object that takes in the new userinfo
        fields = ['username', 'email', 'password1', 'password2']


