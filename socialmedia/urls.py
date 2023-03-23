from django.urls import path
from . import views

app_name = 'socialmedia'

urlpatterns=[path("",views.login,name='login'),
             path("feed/",views.feed,name='feed'),
             path("register/",views.register,name='register'),
             path("upload/",views.upload,name='upload')]
