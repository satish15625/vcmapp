from django.contrib import admin
from .models import Banner,ContactHeader,ProfessionTeam,HappyClients,VendorAds,ServicesOffered,SubscriptionPlans,AboutUs,GalleryContent,OurStatistics,Logo,About_Details
# Register your models here.
admin.site.site_header = 'Villagers Group Admin Panel'
admin.site.site_title="Villagers Group Admin Login"
admin.site.index_title ="Welcome to Villagersgroup Admin"

admin.register(Banner,ContactHeader,ProfessionTeam,VendorAds,HappyClients,ServicesOffered,SubscriptionPlans,AboutUs,GalleryContent,OurStatistics,Logo,About_Details)(admin.ModelAdmin)

