"""
view file for handling rendering action

"""

from django.shortcuts import render, redirect
from .models import Banner, ProfessionTeam, ServicesOffered, HappyClients, AboutUs, SubscriptionPlans,ContactHeader,GalleryContent
from .forms import ConsultingForm
from django.contrib import messages


def index(request):

    # home page for showing banner list and image

    banner = Banner.objects.all()

    professional = ProfessionTeam.objects.all()
    professional1 = ProfessionTeam.objects.all()

    contact = ContactHeader.objects.all().order_by('-id')[:1]

    recentImage = GalleryContent.objects.all().order_by('-id')[:8] 

    # get recent four records for showing services
    services = ServicesOffered.objects.all().order_by('-id')[:4]

    happyclients = HappyClients.objects.all()

    consultingInput = ConsultingForm(None)

    print(happyclients)

    if(request.method == 'POST'):

        consultingInput = ConsultingForm(request.POST)

        if consultingInput.is_valid():

            consultingInput.save()

            messages.add_message(
                request, messages.SUCCESS, 'Thanks! your response submitted successfully. Our support team will connect with you in 24 Hrs.')

            redirect('/')

        else:
            return render(request, "login/index.html", {'form': consultingInput, 'banner': banner, 'professional': professional, 'services': services, 'happyclient': happyclients,'contact':contact,'recent' :recentImage})

    return render(request, 'login/index.html', {'form': consultingInput, 'banner': banner, 'professional': professional, 'services': services, 'happyclient': happyclients,'contact':contact,'recent' :recentImage})


def about(request):
    aboutsContent = AboutUs.objects.all().first()
    plans = SubscriptionPlans.objects.all()
    contact = ContactHeader.objects.all().order_by('-id')[:1]
    recentImage = GalleryContent.objects.all().order_by('-id')[:8] 
    return render(request, 'login/about.html', {'about': aboutsContent, 'plans': plans,'contact' :contact,'recent':recentImage})


def services(request):
    services = ServicesOffered.objects.all()
    contact = ContactHeader.objects.all().order_by('-id')[:1]
    recentImage = GalleryContent.objects.all().order_by('-id')[:8] 
    return render(request, 'login/services.html', {"services": services,'contact' : contact,'recent':recentImage})


def contact(request):

    consultingInput = ConsultingForm(None)

    contact = ContactHeader.objects.all().order_by('-id')[:1]

    recentImage = GalleryContent.objects.all().order_by('-id')[:8] 

    if(request.method == 'POST'):
        print(request.POST)
        consultingInput = ConsultingForm(request.POST)

        if consultingInput.is_valid():

            consultingInput.save()

            messages.add_message(
                request, messages.SUCCESS, 'Thanks! your response submitted successfully. Our support team will connect with you in 24 Hrs.')

            redirect('/contact')

        else:
            return render(request, "login/contact.html", {'form': consultingInput,'contact':contact,'recent':recentImage})

    return render(request, 'login/contact.html', {'form': consultingInput,'contact':contact,'recent':recentImage})


def gallery(request):

    """
    view class for handling gellery section results based on the cateogory specified
    """
    if (request.GET.get('cat') is None) or (request.GET.get('cat') == '0') :
        category = '0'
        gallery = GalleryContent.objects.all()
    else:
        category = request.GET['cat']
        gallery = GalleryContent.objects.filter(image_category=category)
    
    recentImage = GalleryContent.objects.all().order_by('-id')[:8] 

    contact = ContactHeader.objects.all().order_by('-id')[:1]

    return render(request, 'login/gallery.html',{'gallery':gallery,'category':category,'recent':recentImage,'contact':contact})
