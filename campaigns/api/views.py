from rest_framework.decorators import api_view
from rest_framework.response import Response

from campaigns.api import serializers


@api_view(http_method_names=['get'])
def campaigns_view(request, **kwargs):
    serializer = serializers.CampaignSerializer()
    return Response(serializer.all())


@api_view(http_method_names=['get'])
def campaign_view(request, campaign_id, **kwargs):
    serializer = serializers.SingleCampaignSerializer()
    return Response(serializer.get_campaign(campaign_id))


@api_view(http_method_names=['get'])
def campaign_leads_view(request, campaign_id, **kwargs):
    serializer = serializers.LeadSerializer()
    return Response(serializer.filter(campaign_id))
