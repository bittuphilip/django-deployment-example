from django.shortcuts import render

# Create your views here.

from . import forms


def index(request):
    return render(request,'forms_basic/index.html')


def forms_name_view(request):
    form = forms.FormName()
    
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        
        if(form.is_valid()):
            
            print("Validation Success!")
            print("NAME:",form.cleaned_data['name'])
            print("EMAIl:",form.cleaned_data['email'])
            print("TEXT:",form.cleaned_data['text'])
    
    return render(request,'forms_basic/basicForms.html',{'form':form})