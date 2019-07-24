from django.shortcuts import render

def index(request):
    return render(request,'login/index.html')

def about(request):
    return render(request,'login/about.html')

def services(request):
    return render(request, 'login/services.html')

def contact(request):
    return render(request, 'login/contact.html')

def gallery(request):
    return render(request, 'login/gallery.html')
