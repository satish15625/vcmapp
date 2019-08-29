from django.contrib import admin
from django.contrib.auth.models import User

from .models import Banner, ContactHeader, ProfessionTeam, HappyClients, VendorAds, ServicesOffered, SubscriptionPlans, AboutUs, GalleryContent, OurStatistics, Logo, About_Details
# Register your models here.
admin.site.site_header = 'Villagers Group Admin Panel'
admin.site.site_title = "Villagers Group Admin Login"
admin.site.index_title = "Welcome to Villagersgroup Admin"

admin.register(Banner, ContactHeader, ProfessionTeam, VendorAds, HappyClients, ServicesOffered,
               SubscriptionPlans, AboutUs, GalleryContent, OurStatistics, Logo, About_Details)(admin.ModelAdmin)

admin.site.unregister(User)
@admin.register(User)
class SaleSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/sale_summary_change_list.html'

    def changelist_view(self, request, extra_context=None):
            response = super().changelist_view(
                request,
                extra_context=extra_context,
            )
            try:
                qs = response.context_data['cl'].queryset
            except (AttributeError, KeyError):
                return response

          
            response.context_data['summary'] = list(
                qs
                .values('email')
                .order_by('-id')
            )

            return response
