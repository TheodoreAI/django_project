from django.shortcuts import render
# importing the Post class from the models module
from .models import Post

# list of dictionaries for blog content
posts = [
    {
        'author': 'Joe Goldberg',
        'title': 'Blog post 1',
        'content': 'first post content',
        'date_posted': 'March 20, 2020'
    },
    {
        'author': 'Max Paine',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'March 19, 2020'
    }
]
# Create your views here.
def home(request):
    """Passes info into the template"""

    # dict
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def login(request):
    """This is used to add the login.html file (rwk)"""
    return render(request, 'blog/login.html', {'title': 'Login'})




