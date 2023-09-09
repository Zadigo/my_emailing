from django.contrib import admin

from campaigns.models import Campaign, Lead, Sequence


class CampaignAdmin(admin.ModelAdmin):
    list_display = ['name']


class SequenceAdmin(admin.ModelAdmin):
    list_display = ['sequence_id']


class LeadAdmin(admin.ModelAdmin):
    list_display = ['email', 'firstname',
                    'lastname', 'completion_date', 'completed']
    date_hierarchy = 'created_on'
    list_per_page = 10


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Sequence, SequenceAdmin)
admin.site.register(Lead, LeadAdmin)
