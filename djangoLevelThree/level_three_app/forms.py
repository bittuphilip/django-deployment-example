'''
Created on Dec 9, 2019

@author: bitphili0
'''
from django import forms
from level_three_app.models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        