from rest_framework import fields
from rest_framework.serializers import Serializer
from campaigns.models import Campaign, Lead
from django.shortcuts import get_object_or_404


class SequenceSerializer(Serializer):
    id = fields.IntegerField()
    sequence_id = fields.CharField()
    number_of_days = fields.IntegerField()
    email_object = fields.CharField()
    email_text = fields.CharField()
    html_text = fields.CharField()
    get_vue_absolute_url = fields.CharField()


class LeadSerializer(Serializer):
    id = fields.IntegerField()
    firstname = fields.CharField()
    lastname = fields.CharField()
    full_name = fields.CharField()
    email = fields.EmailField()
    completed = fields.BooleanField()
    completion_date = fields.DateTimeField()
    modified_on = fields.DateTimeField()
    created_on = fields.DateTimeField()

    def filter(self, campaign_id):
        campaign = get_object_or_404(Campaign, campaign_id=campaign_id)
        leads = campaign.lead_set.all()
        serializer = LeadSerializer(instance=leads, many=True)
        return serializer.data


class CampaignSerializer(Serializer):
    id = fields.IntegerField()
    campaign_id = fields.CharField()
    name = fields.CharField()
    number_of_leads = fields.IntegerField()
    modified_on = fields.DateTimeField()
    created_on = fields.DateTimeField()
    get_vue_absolute_url = fields.CharField()

    def all(self):
        queryset = Campaign.objects.all()
        serializer = CampaignSerializer(instance=queryset, many=True)
        return serializer.data


class SingleCampaignSerializer(Serializer):
    id = fields.IntegerField()
    campaign_id = fields.CharField()
    name = fields.CharField()
    # lead_set = LeadSerializer(many=True)
    number_of_leads = fields.IntegerField()
    modified_on = fields.DateTimeField()
    created_on = fields.DateTimeField()
    sequence_set = SequenceSerializer(many=True)
    start_date = fields.DateTimeField()
    active = fields.BooleanField()
    archived = fields.BooleanField()
    get_vue_absolute_url = fields.CharField()

    def get_campaign(self, campaign_id):
        queryset = Campaign.objects.get(campaign_id=campaign_id)
        serializer = SingleCampaignSerializer(instance=queryset)
        return serializer.data
