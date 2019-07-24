from django.shortcuts import render

def index(request):
    return render(request,'login/index.html')

def about(request):
    return render(request,'login/about.html')
