from django.contrib import admin

from campaigns.models import Campaign, Lead, Sequence, Schedule


class CampaignAdmin(admin.ModelAdmin):
    list_display = ['name']


class SequenceAdmin(admin.ModelAdmin):
    list_display = ['sequence_id', 'number_of_days']


class LeadAdmin(admin.ModelAdmin):
    list_display = ['email', 'firstname',
                    'lastname', 'completion_date', 'completed']
    date_hierarchy = 'created_on'
    list_per_page = 10


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['campaign', 'name', 'start_time_at', 'end_time_at']
    date_hierarchy = 'created_on'
    list_per_page = 10


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Sequence, SequenceAdmin)
admin.site.register(Lead, LeadAdmin)
admin.site.register(Schedule, ScheduleAdmin)
