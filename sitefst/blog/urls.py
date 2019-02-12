# from django.test import TestCase
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
# Create your tests here.