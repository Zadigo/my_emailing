from django.core.validators import FileExtensionValidator
from django.utils.crypto import get_random_string
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas
from campaigns import models
from campaigns.api import serializers
from rest_framework.exceptions import NotAcceptable


@api_view(http_method_names=['get'])
def campaigns_view(request, **kwargs):
    """Returns all the campaigns for a given team"""
    serializer = serializers.CampaignSerializer()
    return Response(serializer.all())


@api_view(http_method_names=['get'])
def campaign_view(request, campaign_id, **kwargs):
    """Returns the details of a single campaign"""
    serializer = serializers.SingleCampaignSerializer()
    return serializer.get_campaign(campaign_id)


@api_view(http_method_names=['post'])
def create_campaign_view(request, **kwargs):
    """Creates a new campaign"""
    params = {'name': f'Campaign_{get_random_string(5)}'}
    campaign = models.Campaign.objects.create(**params)
    serializer = serializers.SingleCampaignSerializer(instance=campaign)
    return Response(serializer.data)


@api_view(http_method_names=['post'])
def update_campaign_view(request, campaign_id, **kwargs):
    """Updates a current campaign"""
    serializer = serializers.ValidateCampaignUpdate(data=request.POST)
    serializer.is_valid(raise_exception=True)
    return serializer.update(campaign_id)


@api_view(http_method_names=['get'])
def leads_view(request, campaign_id, **kwargs):
    serializer = serializers.LeadSerializer()
    return serializer.filter(campaign_id)


@api_view(http_method_names=['get'])
def lead_view(request, campaign_id, lead_id, **kwargs):
    serializer = serializers.LeadSerializer()
    return serializer.get_lead(campaign_id, lead_id)


@api_view(http_method_names=['post'])
def create_lead_view(request, campaign_id, **kwargs):
    """Adds new leads to campaign either by sending an email
    or by using a file containing a list of emails"""
    csv_file = request.FILES.get('csv_file', None)
    if csv_file is not None:
        validator = FileExtensionValidator(allowed_extensions=['csv'])
        validator(csv_file)
        df = pandas.read_csv(csv_file)
        if 'email' not in df.columns:
            raise NotAcceptable(detail='Missing column email')
        df.sort_values('email', inplace=True)
    else:
        serializer = serializers.ValidateNewLeadSerializer(data=request.POST)
    return Response({})


@api_view(http_method_names=['post'])
def create_lead_view(request, campaign_id, lead_id, **kwargs):
    """Adds new leads to campaign either by sending an email
    or by using a file containing a list of emails"""
    serializer = serializers.ValidateUpdateLeadSerializer(data=request.POST)
    serializer.is_valid(raise_exception=True)
    return serializer
