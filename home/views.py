"""
view file for handling rendering action

"""

from django.shortcuts import render, redirect
from .models import Banner, ProfessionTeam, ServicesOffered, HappyClients, AboutUs, SubscriptionPlans, VendorAds, ContactHeader, GalleryContent, About_Details, OurStatistics, Logo, Profile
from .forms import ConsultingForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.conf import settings
from django.core.validators import validate_email, ValidationError
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from uuid import uuid4
import hashlib
import random


"""
django view function for handling custom login 

"""


@user_passes_test(lambda user: not user.username, login_url='/successpage', redirect_field_name=None)
def index(request):

    # home page for showing banner list and image
    logo = Logo.objects.all().first()
    banner = Banner.objects.all()

    professional = ProfessionTeam.objects.all()
    professional1 = ProfessionTeam.objects.all()

    contact = ContactHeader.objects.all().order_by('-id')[:1]

    recentImage = GalleryContent.objects.all().order_by('-id')[:8]
    about_details = About_Details.objects.all().order_by('-id')[:1]
    # get recent four records for showing services
    services = ServicesOffered.objects.all().order_by('-id')[:4]
    statistics = OurStatistics.objects.all()

    vendorAds = VendorAds.objects.all().order_by('-id')

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
            return render(request, "login/index.html", {'form': consultingInput, 'banner': banner, 'professional': professional, 'services': services, 'happyclient': happyclients, 'contact': contact, 'recent': recentImage, 'about_details': about_details, 'statistics': statistics, 'logo': logo, 'vendorAds': vendorAds})

    return render(request, 'login/index.html', {'form': consultingInput, 'banner': banner, 'professional': professional, 'services': services, 'happyclient': happyclients, 'contact': contact, 'recent': recentImage, 'about_details': about_details, 'statistics': statistics, 'logo': logo, 'vendorAds': vendorAds})


@user_passes_test(lambda user: not user.username, login_url='/successpage', redirect_field_name=None)
def about(request):
    logo = Logo.objects.all().first()
    aboutsContent = AboutUs.objects.all().first()
    plans = SubscriptionPlans.objects.all()
    contact = ContactHeader.objects.all().order_by('-id')[:1]
    recentImage = GalleryContent.objects.all().order_by('-id')[:8]
    about_details = About_Details.objects.all().order_by('-id')[:1]
    return render(request, 'login/about.html', {'about': aboutsContent, 'plans': plans, 'contact': contact, 'recent': recentImage, 'about_details': about_details, 'logo': logo})


@user_passes_test(lambda user: not user.username, login_url='/successpage', redirect_field_name=None)
def services(request):
    logo = Logo.objects.all().first()
    services = ServicesOffered.objects.all()
    contact = ContactHeader.objects.all().order_by('-id')[:1]
    recentImage = GalleryContent.objects.all().order_by('-id')[:8]
    statistics = OurStatistics.objects.all()
    about_details = About_Details.objects.all().order_by('-id')[:1]
    return render(request, 'login/services.html', {"services": services, 'contact': contact, 'recent': recentImage, 'statistics': statistics, 'about_details': about_details, 'logo': logo})


@user_passes_test(lambda user: not user.username, login_url='/successpage', redirect_field_name=None)
def contact(request):
    logo = Logo.objects.all().first()
    consultingInput = ConsultingForm(None)

    contact = ContactHeader.objects.all().order_by('-id')[:1]

    recentImage = GalleryContent.objects.all().order_by('-id')[:8]
    about_details = About_Details.objects.all().order_by('-id')[:1]
    if(request.method == 'POST'):
        print(request.POST)
        consultingInput = ConsultingForm(request.POST)

        if consultingInput.is_valid():

            consultingInput.save()

            messages.add_message(
                request, messages.SUCCESS, 'Thanks! your response submitted successfully. Our support team will connect with you in 24 Hrs.')

            redirect('/contact')

        else:
            return render(request, "login/contact.html", {'form': consultingInput, 'contact': contact, 'recent': recentImage, 'about_details': about_details, 'logo': logo})

    return render(request, 'login/contact.html', {'form': consultingInput, 'contact': contact, 'recent': recentImage, 'about_details': about_details, 'logo': logo})


@user_passes_test(lambda user: not user.username, login_url='/successpage', redirect_field_name=None)
def gallery(request):
    """
    view class for handling gellery section results based on the cateogory specified
    """
    if (request.GET.get('cat') is None) or (request.GET.get('cat') == '0'):
        category = '0'
        gallery = GalleryContent.objects.all()
    else:
        category = request.GET['cat']
        gallery = GalleryContent.objects.filter(image_category=category)

    recentImage = GalleryContent.objects.all().order_by('-id')[:8]
    logo = Logo.objects.all().first()
    contact = ContactHeader.objects.all().order_by('-id')[:1]
    about_details = About_Details.objects.all().order_by('-id')[:1]

    return render(request, 'login/gallery.html', {'gallery': gallery, 'category': category, 'recent': recentImage, 'contact': contact, 'about_details': about_details, 'logo': logo})


def sendUserEmail(request):
    try:

        if 'type' not in request.GET:
            raise ValueError('Type field is required')

        if 'email' not in request.GET or (request.GET.get('email') == ""):
            raise ValueError('Email field is required')

        validate_email(request.GET['email'])

        if request.GET.get('type') == 'subscription':
            # send subscription email to user about the thank you note and email to admin about the information.
            email = request.GET.get('email')
            subject = "Thank You for subscribing our daily news"
            message = "You are now part of our daily services and offers. We will share you daily updated of our activity"
            email = EmailMessage(subject, message, to=[email])
            email.send()

        # send email to admin as well
        emailAdmin = settings.DEFAULT_FROM_EMAIL
        subjectAdmin = "New user subscription reminder"
        messageAdmin = "New user has subscribed for newsletter :" + \
            request.GET['email']
        emailAdmin = EmailMessage(subjectAdmin, messageAdmin, to=[emailAdmin])
        emailAdmin.send()

        response = {'code': 200,
                    'message': "Thanks! Your have subscribed for daily updates"}

    except ValueError as error:

        response = {'code': 422, 'message': str(error)}

    except ValidationError as error:
        response = {'code': 422, 'message': str(error.message)}

    except Exception as error:
        response = {'code': 422, 'message': str(error)}

    return JsonResponse(response)


"""
login method to for handling user login session 
"""


def UserLogin(request):
    logout(request)
    username = password = ''
    company_name = request.POST['username']
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']

        try:
            
            username = User.objects.get(username = email.lower()+'_'+company_name)
          

        except User.DoesNotExist:
            username = None

        if not username:

            # store new registered user into the db.
            username = email + '_' + company_name
            UserObject = User.objects.create_user(
                email=email.lower(), password=password, username=username)

            # store profile information
           
            phone_number = request.POST['phone']
            sha12_password = hashlib.sha256(
                str.encode(request.POST['password'])).hexdigest()
            Profile.objects.create(
                user=UserObject, company_name=company_name, phone_number=phone_number, password=sha12_password)

            # send email to client about the url and password to login.

            email = request.POST.get('email')
            subject = "Welcome To VCM Team. Login detail for shopping portal"
            message = """
                            You are now part of our team and we appreciate your efforts to be part our valuable team use below detail to
                            get started with adding your products.

                            email : %s

                            password : %s

                            click here to log in into store panel http://www.villagersgroup.com/shoppingportal/store
                              

                      """ % (request.POST.get('email'), request.POST.get('password'))

            email = EmailMessage(subject, message, to=[email])
            email.send()

            #send email to admin about the new joining
                
            emailAdmin = settings.DEFAULT_FROM_EMAIL
            subjectAdmin = "New user joined shopping portal"
            messageAdmin = "New user has recently joined :" + request.POST['email']
            emailAdmin = EmailMessage(subjectAdmin, messageAdmin, to=[emailAdmin])
            emailAdmin.send()

        user = authenticate(username=username, password=password)

        if user is not None:
            #login(request, user)
            return redirect('/successpage')
        else:
            messages.add_message(
                request, messages.WARNING, 'Your account credentials are not valid')


#@login_required(login_url='/')
def dashboard(request):
    return render(request, 'dashboard/index.html')


@login_required(login_url='/')
def userLogout(request):
    logout(request)
    return redirect('/')
