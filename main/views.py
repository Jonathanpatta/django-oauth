from main.models import UserProfile,Blog,Activity
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    user = request.user
    picture = "https://thumbs.dreamstime.com/b/default-avatar-profile-icon-vector-social-media-user-portrait-176256935.jpg"
    is_logged_in = False
    user_profile = None
    if(request.user.is_authenticated):

        user_profile = UserProfile.objects.get(user=user)
    
    if(user.is_authenticated):
        
        picture = user_profile.avatar_url
        is_logged_in = True
    

    blogs = Blog.objects.all()
    

    context = {
        "user": user_profile,
        "blogs": blogs,
    }
    print(request.user.id)
    return render(request,'main/index.html',context)

@login_required(login_url='/accounts/login/')
def Profile(request):
    up = None
    if request.user.is_authenticated:
        up = UserProfile.objects.get(user=request.user)
    print(up.avatar_url)
    print(dir(up.user))
    print(up.user.socialaccount_set)
    context = {
        "user" : up,
    }
    return render(request,"main/profile.html",context)

def BlogView(request,id):
    up = None
    if request.user.is_authenticated:
        up = UserProfile.objects.get(user=request.user)

    blog = Blog.objects.get(id=id)
    blog.views += 1

   

    if request.user.is_authenticated:
        act = Activity.objects.create(user=request.user,blog=blog,type="view")
    
    blog.save()

    context = {
        "user" : up,
        "blog" : blog,
    }

    return render(request,"main/blog.html",context)

@login_required(login_url='/accounts/login/')
def BlogsView(request):

    up = None
    if request.user.is_authenticated:
        up = UserProfile.objects.get(user=request.user)

    blogs = Blog.objects.filter(author=request.user)

    context = {
        "user" : up,
        "blogs" : blogs,
    }

    return render(request,"main/blogs.html",context)

@login_required(login_url='/accounts/login/')
def HistoryView(request):

    up = None
    if request.user.is_authenticated:
        up = UserProfile.objects.get(user=request.user)

    activities = Activity.objects.filter(user=request.user)

    context = {
        "user" : up,
        "activities" : activities,
    }

    return render(request,"main/history.html",context)