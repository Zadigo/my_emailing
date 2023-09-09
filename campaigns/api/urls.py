from django.urls import re_path

from campaigns.api import views

urlpatterns = [
    re_path(
        r'(?P<campaign_id>camp\_[a-z]+)/leads',
        views.campaign_leads_view
    ),
    re_path(
        r'(?P<campaign_id>camp\_[a-z]+)',
        views.campaign_view
    ),
    re_path(r'^$', views.campaigns_view)
]
