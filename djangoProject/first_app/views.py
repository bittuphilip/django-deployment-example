from django.shortcuts import render


# Create your views here.

 
# def index(request):
# #     return HttpResponse("<em> My Second Project</em>")
#     my_dict={'insert_me':"Hello Iam coming from first_app/index!"}
#     return render(request,"first_app/index.html",context = my_dict)


def image(request):
    img_dict ={'insert_me':"Hello Iam coming from first_app/staticImage.html!"}
    return render(request,"first_app/staticImage.html",context = img_dict)