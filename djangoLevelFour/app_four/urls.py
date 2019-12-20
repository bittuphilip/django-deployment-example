'''
Created on Dec 9, 2019

@author: bitphili0
'''
from django.urls import path
from app_four import views

#Template Tagging

app_name = 'app_four'

urlpatterns = [
    
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
    path('base/',views.base_url,name='base_url'), 
     path('index/',views.base_url,name='index'), 
    ]