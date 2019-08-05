from django.contrib import admin
from .models import Banner,About_Details,ContactHeader,ProfessionTeam,HappyClients,ServicesOffered,SubscriptionPlans,AboutUs,GalleryContent,OurStatistics,Logo
# Register your models here.
admin.site.site_header = 'Villagers Group Admin Panel'
admin.site.site_title="Villagers Group Admin Login"
admin.site.index_title ="Welcome to Villagersgroup Admin"

admin.register(Banner,About_Details,ContactHeader,ProfessionTeam,HappyClients,ServicesOffered,SubscriptionPlans,AboutUs,GalleryContent,OurStatistics,Logo)(admin.ModelAdmin)
