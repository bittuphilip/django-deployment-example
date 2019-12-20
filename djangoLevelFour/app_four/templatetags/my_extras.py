'''
Created on Dec 17, 2019

@author: bitphili0
'''
from django import template


register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts all the value of arg from the string
    """
    
    return value.replace(arg,'')


# register.filter('cut', cut)