from django.db import models

# Create your banner modee


class Banner(models.Model):
    """
    model class for storing banner image

    """
    banner_img = models.ImageField(upload_to='media')
    banner_title = models.CharField(max_length=100)
    banner_desc = models.TextField()
    banner_right_desc = models.TextField()
    read_more_desc = models.TextField()

    class Meta:
        db_table = 'vg_banner'


class ProfessionTeam(models.Model):
    """
    model class for handling contact header informations

    """
    avatar = models.ImageField(upload_to="media")
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=25)
    description = models.TextField(null=True)
    phone_number = models.BigIntegerField()
    country_code = models.CharField(max_length=6)
    contact_email = models.EmailField()
    facebook_url = models.URLField()
    twitter_url = models.URLField()
    insta_url = models.URLField()
    linkedin_url = models.URLField()

    class Meta:
        db_table = 'vg_professional_teaml'


class ContactHeader(models.Model):
    """
    model class for handling contact header informations

    """
    phone_number = models.BigIntegerField()
    country_code = models.CharField(max_length=6)
    contact_email = models.EmailField()
    facebook_url = models.URLField()
    twitter_url = models.URLField()
    insta_url = models.URLField()
    linkedin_url = models.URLField()

    class Meta:
        db_table = 'vg_contact_header'


class ServicesOffered(models.Model):
    """
    service model to store the type of service offered by the company

    """
    service_name = models.CharField(max_length=30)
    service_desc = models.TextField()
    service_image = models.ImageField(upload_to='media')
    service_icon = models.CharField(max_length=200)

    class Meta:
        db_table = 'vg_service_offered'


class HappyClients(models.Model):
    client_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=25)
    avatar = models.ImageField(upload_to='media')
    rating = models.IntegerField()
    description = models.TextField()

    class Meta:
        db_table = 'vg_happy_clients'


class ConsultingCustomer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    number = models.CharField(max_length=20)
    message = models.TextField(null=True,blank=True)

    class Meta:
        db_table = 'vg_consulting_clients'


class AboutUs(models.Model):
    title = models.CharField(max_length=25)
    banner = models.ImageField(upload_to = "media",null=True)
    heading = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    per_mangemt = models.IntegerField()
    per_marketing = models.IntegerField()
    per_stratergy = models.IntegerField()
    per_deployment = models.IntegerField()

    class Meta:
        db_table = "vg_about_us"


class SubscriptionPlans(models.Model):
    plan_name = models.CharField(max_length=25)
    price = models.FloatField()
    currency = models.CharField(max_length=4)
    period = models.CharField(max_length = 15,default="month")
    color_code = models.CharField(max_length=20)
    email_suppport = models.CharField(max_length=50)
    storage_suppport = models.CharField(max_length=50)
    website_suppport = models.CharField(max_length=50)
    bandwidth_suppport = models.CharField(max_length=50)
    customer_suppport = models.CharField(max_length=50)

    class Meta:
        db_table = 'vg_subscription_plan'
