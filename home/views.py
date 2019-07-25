from django.shortcuts import render
from .models import Banner
def index(request):

    banner =Banner.objects.all() 
    return render(request,'login/index.html',{'banner':banner})

def about(request):
    return render(request,'login/about.html')

def services(request):
    return render(request, 'login/services.html')

def contact(request):
    return render(request, 'login/contact.html')

def gallery(request):
    return render(request, 'login/gallery.html')
