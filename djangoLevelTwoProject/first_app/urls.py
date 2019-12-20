'''
Created on Dec 6, 2019

@author: bitphili0
'''
from django.urls import path
from first_app import views

urlpatterns = [
    path('',views.users,name='users'),
]
