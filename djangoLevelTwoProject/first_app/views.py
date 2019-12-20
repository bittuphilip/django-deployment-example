from django.shortcuts import render

# Create your views here.
from first_app.models import User
# from django.http import HttpResponse
from first_app.forms import NewUserForm





def index(request):
    return render(request, 'first_app/index.html')

def users(request):
    form = NewUserForm()
    
    
    if (request.method=='POST'):
        form = NewUserForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return index(request)
        else:
            print("Form Invalid Error!")
    return render(request,"first_app/users.html",{'form':form})
           
            
#     users_list = User.objects.order_by("first_name")
#     user_dict ={'user_records':users_list}
#     return render(request, "first_app/users.html", context = user_dict)
