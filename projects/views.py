from abc import ABC

from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from projects.forms import ContactForm
from django.contrib import messages
from django.http import Http404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


# Create your views here.


def project(request):
    """This is used to make the query: a command that allows me to create, retrieve, update and delete objects in my database.
     objects: everything in the Project class"""
    projects = Project.objects.all()

    context = {
        'projects': projects

    }
    return render(request, 'projects/project.html', context)


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project.html'
    context_object_name = 'projects'

    ordering = ['-date_posted']
    paginate_by = 6


class UserProjectListView(ListView):
    """
    This class is used for the user projects.
    """
    model = Project
    template_name = 'projects/user_projects.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    paginate_by = 6

    def get_queryset(self):
        """If the username exists then it will limit the results to that user"""
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Project.objects.filter(author=user).order_by('-date_posted')


class ProjectDetailView(DetailView):
    model = Project


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'description', 'image', 'technology', 'link', 'github', 'date_posted']
    # this is what sets the author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    # get all the objects from the model Project
    fields = ['title', 'description', 'image', 'technology', 'link', 'github', 'date_posted']

#     setting the author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Makes sure that the user maling the post is signed in"""
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'

    def test_func(self):
        """making sure that the user that is updating is signed in"""

        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False





def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, f'Your message has been sent!')
        return redirect('blog-home')

    return render(request, 'projects/contact.html', {'form': form})
