from django.shortcuts import render
# importing the Post class from the models module
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin

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

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'            # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # changes when the posts are made using the negative sign
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    

    # this is what sets the author
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    

    # this is what sets the author
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

    def test_func(self):
        """ Making sure that the user that is updating the post is signed in and only updating the
        correct posts"""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        """ Making sure that the user that is updating the post is signed in and only updating the
        correct posts"""

        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def login(request):
    """This is used to add the login.html file (rwk)"""
    return render(request, 'blog/login.html', {'title': 'Login'})





