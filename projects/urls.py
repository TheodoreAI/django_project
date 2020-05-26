from django.urls import path

from . import views

# will add stuff to this for adding the projects to the admin page

urlpatterns = [
    path("project_index/", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path('contact/', views.contact, name="contact"),

]
