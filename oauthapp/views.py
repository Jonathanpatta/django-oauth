from django.http import HttpResponse
from django.shortcuts import render
from main.models import UserProfile


def home(request):
    user = request.user
    picture = "https://thumbs.dreamstime.com/b/default-avatar-profile-icon-vector-social-media-user-portrait-176256935.jpg"
    is_logged_in = False
    if(user.is_authenticated):
        user_profile = UserProfile.objects.get(user=user)
        picture = user_profile.avatar_url
        is_logged_in = True
        
    

    context = {
        "user": user.username,
        "is_logged_in": is_logged_in,
        "user_picture_url":picture,
    }
    print(request.user)
    return render(request,'main/index.html',context)
    #return HttpResponse("<h1> hello "+str(request.user)+"<h1>")