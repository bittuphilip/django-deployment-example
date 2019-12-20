from django.db import models

# Create your models here.
from django.forms import ModelForm



class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3,)
    birth_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']