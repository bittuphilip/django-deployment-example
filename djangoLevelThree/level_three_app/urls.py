'''
Created on Dec 9, 2019

@author: bitphili0
'''
'''
Created on Dec 6, 2019

@author: bitphili0
'''
from django.urls import path
from level_three_app import views

urlpatterns = [
    path('',views.users,name='users'),
]
