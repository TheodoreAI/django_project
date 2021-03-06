from django.shortcuts import render, get_object_or_404
# importing the Post class from the models module
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .forms import AboutUpdateForm
from .models import About


# Create your views here.
def home(request):
    """Passes info into the template"""

    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # changes when the posts are made using the negative sign
    ordering = ['-date_posted']
    # the amount of pages that will be showing
    paginate_by = 4


# so that posts form a certain user  are  seen
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # changes when the posts are made using the negative sign
    ordering = ['-date_posted']
    # the amount of pages that will be showing
    paginate_by = 4

    def get_queryset(self):
        """ if the username exists then it will limit the results to that user"""
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by("-date_posted")


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
    context = {
        'about': About.objects.all()
    }
    return render(request, 'blog/about.html', context)
