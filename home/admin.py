from django.contrib import admin
from .models import Banner,ContactHeader,ProfessionTeam,HappyClients,ServicesOffered
# Register your models here.
admin.site.site_header = 'Villagers Group Admin Panel'

admin.register(Banner,ContactHeader,ProfessionTeam,HappyClients,ServicesOffered)(admin.ModelAdmin)
