import pandas
import redis
from django.core.validators import FileExtensionValidator
from django.utils.crypto import get_random_string
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotAcceptable, NotFound
from rest_framework.response import Response
import json
from campaigns import models
from campaigns.api import connections
from campaigns.api import serializers


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


def active_campaign_view(request, campaign_id):
    # instance = connections.get_redis_connection()
    try:
        campaign = models.Campaign.objects.get(campaign_id=campaign_id)
    except:
        raise NotFound(message='Campaign does not exist')
    else:
        campaign.active = False if campaign.active else True
        campaign.save()

        # schedules = campaign.schedule_set.values()
        # schedules = json.dumps(schedules)
        
        # instance.hset(campaign_id, 'active', campaign.active)
        # instance.hset(campaign_id, 'schedules', schedules)

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

    response, campaign = serializer.update(campaign_id)

    # If the campaign is activated, we need to
    # is_active = serializer.validated_data.get('active')
    # connection = connections.get_redis_connection()
    # if is_active:
    #     if connection:
    #         connection.hset(campaign.campaign_id, '', {})
    # else:
    #     if connection:
    #         connection.hdel(campaign.campaign_id)
    return response


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
def review_leads_view(request, campaign_id, **kwargs):
    serializer = serializers.ValidateReviewLeadsSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return serializer.save(campaign_id)


@api_view(http_method_names=['post'])
def create_lead_view(request, campaign_id, lead_id, **kwargs):
    """Adds new leads to campaign either by sending an email
    or by using a file containing a list of emails"""
    serializer = serializers.ValidateUpdateLeadSerializer(data=request.POST)
    serializer.is_valid(raise_exception=True)
    return serializer


@api_view(http_method_names=['post'])
def create_schedule_view(request, campaign_id, **kwargs):
    """Adds new schedule to campaign"""
    serializer = serializers.ValidateScheduleSerializer(data=request.POST)
    serializer.is_valid(raise_exception=True)
    return serializer.save(campaign_id)
