from django.urls import path
from . import views 

# This is used to add the urls to the app 'blog' 
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('login/', views.login, name='blog-login'),
    


]
