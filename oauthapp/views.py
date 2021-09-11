from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
        "user": request.user.username,
        "is_logged_in": True,
    }
    return render(request,'main/index.html',context)
    #return HttpResponse("<h1> hello "+str(request.user)+"<h1>")