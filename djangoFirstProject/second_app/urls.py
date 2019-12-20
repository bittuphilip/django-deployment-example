'''
Created on Dec 3, 2019

@author: bitphili0
'''


from django.urls import path
from second_app import views

urlpatterns = [
    path('', views.help,name='help'),
    ]