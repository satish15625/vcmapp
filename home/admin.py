from django.contrib import admin
from .models import Banner
# Register your models here.
admin.site.site_header = 'Villagers Grop Admin'

admin.site.register(Banner)
