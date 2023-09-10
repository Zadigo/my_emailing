from django.urls import re_path

from campaigns.api import views

urlpatterns = [
    re_path(
        r'^(?P<campaign_id>camp\_[a-zA-Z0-9]+)/leads/(?P<lead_id>\d+)$',
        views.lead_view
    ),
    re_path(
        r'^(?P<campaign_id>camp\_[a-zA-Z0-9]+)/leads/create$',
        views.create_lead_view
    ),
    re_path(
        r'^(?P<campaign_id>camp\_[a-zA-Z0-9]+)/leads/review$',
        views.review_leads_view
    ),
    re_path(
        r'^(?P<campaign_id>camp\_[a-zA-Z0-9]+)/leads$',
        views.leads_view
    ),
    re_path(
        r'^(?P<campaign_id>camp\_[a-zA-Z0-9]+)/schedule$',
        views.create_schedule_view
    ),
    re_path(
        r'^(?P<campaign_id>camp\_[a-zA-Z0-9]+)/update$',
        views.update_campaign_view
    ),
    re_path(
        r'^(?P<campaign_id>camp\_[a-zA-Z0-9]+)$',
        views.campaign_view
    ),
    re_path(r'^new$', views.create_campaign_view),
    re_path(r'^$', views.campaigns_view)
]
