'''
Created on Dec 6, 2019

@author: bitphili0
'''
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoLevelTwoProject.settings')

import django
# Import settings
django.setup()

import random
from first_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_first_name = fakegen.name()
       
        fake_email = fakegen.email()

        # Create new User Entry
        user = User.objects.get_or_create( first_name=fake_first_name, email=fake_email)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
