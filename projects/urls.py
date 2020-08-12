from django.urls import path
from .views import contact

from .views import (

    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    UserProjectListView
)

# will add stuff to this for adding the projects to the admin page

urlpatterns = [
    path('', ProjectListView.as_view(), name="projects-project"),
    path("project/<str:username>", UserProjectListView.as_view(), name='user-projects'),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
    path('projects/new/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('contact/', contact, name="contact"),
]
