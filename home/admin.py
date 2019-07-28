from django.contrib import admin
from .models import Banner,ContactHeader,ProfessionTeam,HappyClients,ServicesOffered,SubscriptionPlans,AboutUs,GalleryContent,OurStatistics,Logo
# Register your models here.
admin.site.site_header = 'Villagers Group Admin Panel'

admin.register(Banner,ContactHeader,ProfessionTeam,HappyClients,ServicesOffered,SubscriptionPlans,AboutUs,GalleryContent,OurStatistics,Logo)(admin.ModelAdmin)
