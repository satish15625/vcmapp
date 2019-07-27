"""
view file for handling rendering action

"""


from django.shortcuts import render, redirect
from .models import Banner, ProfessionTeam, ServicesOffered, HappyClients,AboutUs,SubscriptionPlans
from .forms import ConsultingForm
from django.contrib import messages


def index(request):

    # home page for showing banner list and image

    banner = Banner.objects.all()

    professional = ProfessionTeam.objects.all()
    professional1 = ProfessionTeam.objects.all()

    services = ServicesOffered.objects.all()

    happyclients = HappyClients.objects.all()

    consultingInput = ConsultingForm(None)

    print(happyclients)

    if(request.method == 'POST'):

        consultingInput = ConsultingForm(request.POST)

        if consultingInput.is_valid():

            consultingInput.save()

            messages.add_message(request, messages.SUCCESS, 'Thanks! your response submitted successfully. Our support team will connect with you in 24 Hrs.')

            redirect('/')

        else:
            return render(request, "login/index.html", {'form': consultingInput, 'banner': banner, 'professional': professional, 'services': services, 'happyclient': happyclients})

    return render(request, 'login/index.html', {'form': consultingInput, 'banner': banner, 'professional': professional, 'services': services, 'happyclient': happyclients})


def about(request):
    aboutsContent = AboutUs.objects.all().first()
    plans         = SubscriptionPlans.objects.all()
    return render(request, 'login/about.html',{'about' : aboutsContent,'plans' : plans})


def services(request):
    return render(request, 'login/services.html')


def contact(request):
    return render(request, 'login/contact.html')


def gallery(request):
    return render(request, 'login/gallery.html')
