"""
view file for handling rendering action

"""


from django.shortcuts import render
from .models import Banner, ProfessionTeam, ServicesOffered, HappyClients


def index(request):

    # home page for showing banner list and image
    banner = Banner.objects.all()

    professional = ProfessionTeam.objects.all()

    services = ServicesOffered.objects.all()

    happyclients = HappyClients.objects.all()

    return render(request, 'login/index.html', {'banner': banner, 'professional': professional, 'services' : services, 'happyclient' : happyclients})


def about(request):
    return render(request, 'login/about.html')


def services(request):
    return render(request, 'login/services.html')


def contact(request):
    return render(request, 'login/contact.html')


def gallery(request):
    return render(request, 'login/gallery.html')
