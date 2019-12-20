'''
Created on Dec 1, 2019

@author: bitphili0
'''

from first_app import views

from django.urls import path

urlpatterns = [
#     path('', views.index,name='index'),
    path('', views.index,name='index')
    ]