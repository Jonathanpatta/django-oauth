from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> hello "+str(request.user)+"<h1>")