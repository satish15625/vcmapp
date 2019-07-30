"""
view file for handling rendering action

"""

from django.shortcuts import render, redirect
from .models import Banner, ProfessionTeam, ServicesOffered, HappyClients, AboutUs, SubscriptionPlans,ContactHeader,GalleryContent,About_Details,OurStatistics,Logo
from .forms import ConsultingForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import JsonResponse


def index(request):

    # home page for showing banner list and image
    logo = Logo.objects.all().first()
    banner = Banner.objects.all()

    professional = ProfessionTeam.objects.all()
    professional1 = ProfessionTeam.objects.all()

    contact = ContactHeader.objects.all().order_by('-id')[:1]

    recentImage = GalleryContent.objects.all().order_by('-id')[:8] 
    about_details= About_Details.objects.all().order_by('-id')[:1]
    # get recent four records for showing services
    services = ServicesOffered.objects.all().order_by('-id')[:4]
    statistics = OurStatistics.objects.all()

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
            return render(request, "login/index.html", {'form': consultingInput, 'banner': banner, 'professional': professional, 'services': services, 'happyclient': happyclients,'contact':contact,'recent' :recentImage,'about_details':about_details,'statistics':statistics,'logo':logo})

    return render(request, 'login/index.html', {'form': consultingInput, 'banner': banner, 'professional': professional, 'services': services, 'happyclient': happyclients,'contact':contact,'recent' :recentImage,'about_details':about_details,'statistics':statistics,'logo':logo})


def about(request):
    logo = Logo.objects.all().first()
    aboutsContent = AboutUs.objects.all().first()
    plans = SubscriptionPlans.objects.all()
    contact = ContactHeader.objects.all().order_by('-id')[:1]
    recentImage = GalleryContent.objects.all().order_by('-id')[:8]
    about_details= About_Details.objects.all().order_by('-id')[:1]
    return render(request, 'login/about.html', {'about': aboutsContent, 'plans': plans,'contact' :contact,'recent':recentImage,'about_details':about_details,'logo':logo})


def services(request):
    logo = Logo.objects.all().first()
    services = ServicesOffered.objects.all()
    contact = ContactHeader.objects.all().order_by('-id')[:1]
    recentImage = GalleryContent.objects.all().order_by('-id')[:8] 
    statistics = OurStatistics.objects.all()
    about_details= About_Details.objects.all().order_by('-id')[:1]
    return render(request, 'login/services.html', {"services": services,'contact' : contact,'recent':recentImage,'statistics':statistics,'about_details':about_details,'logo':logo})


def contact(request):
    logo = Logo.objects.all().first()
    consultingInput = ConsultingForm(None)

    contact = ContactHeader.objects.all().order_by('-id')[:1]

    recentImage = GalleryContent.objects.all().order_by('-id')[:8] 
    about_details= About_Details.objects.all().order_by('-id')[:1]
    if(request.method == 'POST'):
        print(request.POST)
        consultingInput = ConsultingForm(request.POST)

        if consultingInput.is_valid():

            consultingInput.save()

            messages.add_message(
                request, messages.SUCCESS, 'Thanks! your response submitted successfully. Our support team will connect with you in 24 Hrs.')

            redirect('/contact')

        else:
            return render(request, "login/contact.html", {'form': consultingInput,'contact':contact,'recent':recentImage,'about_details':about_details,'logo':logo})

    return render(request, 'login/contact.html', {'form': consultingInput,'contact':contact,'recent':recentImage,'about_details':about_details,'logo':logo})


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
    logo = Logo.objects.all().first()
    contact = ContactHeader.objects.all().order_by('-id')[:1]
    about_details= About_Details.objects.all().order_by('-id')[:1]

    return render(request, 'login/gallery.html',{'gallery':gallery,'category':category,'recent':recentImage,'contact':contact,'about_details':about_details,'logo':logo})

def sendUserEmail(request):
    try:
        email = EmailMessage('Subject', 'Body', to=['jatin@yopmail.com'])
        email.send()
    except Exception as error:
        response = {'code':422,'message':str(error)}
  
    return JsonResponse({'code' : 200,'message' : 'Email send successfully'})
