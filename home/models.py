from django.db import models

# Create your banner modee
class Banner(models.Model):
    banner_img = models.ImageField(upload_to='media')
    banner_title = models.CharField(max_length=100)
    banner_desc = models.TextField() 
    banner_right_desc = models.TextField()
    read_more_desc =  models.TextField()

    class Meta:
        db_table = 'vg_banner'

    
class ProfessionTeam(models.Model):
    """
    model class for handling contact header informations

    """
    avatar       = models.ImageField(upload_to = "media")
    name         = models.CharField(max_length = 50)
    designation  = models.CharField(max_length = 25)
    description  = models.TextField(null=True)
    phone_number = models.BigIntegerField()
    country_code = models.CharField(max_length=6)
    contact_email = models.EmailField()
    facebook_url  = models.URLField()
    twitter_url  = models.URLField()
    insta_url    = models.URLField()
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
    facebook_url  = models.URLField()
    twitter_url  = models.URLField()
    insta_url    = models.URLField()
    linkedin_url = models.URLField()

    class Meta:
        db_table = 'vg_contact_header'

