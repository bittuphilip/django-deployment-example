'''
Created on Dec 6, 2019

@author: bitphili0
'''
from django import forms
from django.core import validators

# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label='Enter your Email Again')
#     text = forms.CharField(widget =forms.Textarea)
#     botcaptcher = forms.CharField(required=False,widget =forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    

#     def clean_botcaptcher(self):
#         botcaptcher = self.cleaned_data['botcaptcher']
#         if(len(botcaptcher)>0):
#             raise forms.ValidationError("Got the BOT")
#         return botcaptcher

# 
#     def clean(self):
#         all_clean_data = super().clean()
#         email = all_clean_data['email']
#         vemail = all_clean_data['verify_email']
#         
#         if email!=vemail:
#             raise forms.ValidationError("Make sure Emails are Same!")
#         
#     

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    title = forms.CharField(
        max_length=3,
        widget=forms.Select(),
    )
    birth_date = forms.DateField(required=False)
    
    