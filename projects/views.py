from django.shortcuts import render, redirect
from projects.models import Project
from projects.forms import ContactForm
from django.contrib import messages
from django.http import Http404
# Create your views here.


def project_index(request):
    """This is used to make the query: a command that allows me to create, retrieve, update and delete objects in my database.
     objects: everything in the Project class"""
    projects = Project.objects.all()

    context = {
        'projects': projects

    }
    return render(request, 'projects/project_index.html', context)


def project_detail(request, pk):
    """
    This query retrieves the project with the primary key, pk, equal to that in the function argument.
    """
    project = Project.objects.get(pk=pk)
    context = {
        'project': project

    }
    return render(request, 'projects/project_detail.html', context)



def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():

        form.save()
        messages.success(request, f'Your message has been sent!')
        return redirect('blog-home')

    return render(request, 'projects/contact.html', {'form': form})


