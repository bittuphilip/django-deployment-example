from django.shortcuts import render

# Create your views here.

def help(request):
    
    help_dict={'insert_content':"Hello Iam coming from second_app"}
    return render(request,"second_app/help.html",context = help_dict)
