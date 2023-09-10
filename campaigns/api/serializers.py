import datetime
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import fields
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from campaigns.choices import TimeZoneChoices
from campaigns.models import Campaign, Lead


class ScheduleSerializer(Serializer):
    id = fields.IntegerField()
    schedule_id = fields.CharField()
    start_time_at = fields.TimeField()
    end_time_at = fields.TimeField()
    interval = fields.IntegerField()
    sending_days = fields.JSONField()
    modified_on = fields.DateTimeField()
    created_on = fields.DateTimeField()


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
    reviewed = fields.BooleanField()
    completion_date = fields.DateTimeField()
    modified_on = fields.DateTimeField()
    created_on = fields.DateTimeField()

    def filter(self, campaign_id):
        # campaign = get_object_or_404(Campaign, campaign_id=campaign_id)
        # leads = campaign.lead_set.all()
        # serializer = LeadSerializer(instance=leads, many=True)
        # return serializer.data
        try:
            campaign = Campaign.objects.get(campaign_id=campaign_id)
        except:
            raise NotFound(detail='Campaign not found')
        else:
            leads = campaign.lead_set.all()
            serializer = LeadSerializer(instance=leads, many=True)
            return Response(serializer.data)

    def get_lead(self, campaign_id, lead_id):
        try:
            campaign = Campaign.objects.get(campaign_id=campaign_id)
        except:
            raise NotFound(detail='Campaign not found')
        else:
            lead = campaign.lead_set.filter(id=lead_id)
            if not lead.exists():
                raise NotFound(detail='Lead not found')
            serializer = LeadSerializer(instance=lead.get())
            return Response(serializer.data)


class CampaignSerializer(Serializer):
    id = fields.IntegerField()
    campaign_id = fields.CharField()
    name = fields.CharField()
    number_of_leads = fields.IntegerField()
    sequence_set = SequenceSerializer(many=True)
    schedule_set = ScheduleSerializer(many=True)
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
        try:
            campaign = Campaign.objects.get(campaign_id=campaign_id)
        except:
            raise NotFound(detail='Campaign not found', code=404)
        else:
            serializer = SingleCampaignSerializer(instance=campaign)
            return Response(serializer.data)


class ValidateCampaignUpdate(Serializer):
    name = fields.CharField()
    # sender = None
    # debut_sending_time = None
    # end_sending_time = None
    campaign_timezone = fields.CharField(default='UTC')
    archived = fields.BooleanField(default=False)
    active = fields.BooleanField(default=False)

    def update(self, campaign_id):
        try:
            campaign = Campaign.objects.get(campaign_id=campaign_id)
        except:
            raise NotFound(detail='Campaign not found')
        else:
            validated_data = self.validated_data.copy()
            selected_timezone = validated_data.pop('campaign_timezone')
            for key, value in validated_data.items():
                setattr(campaign, key, value)
            selected_timezone = TimeZoneChoices.choice(selected_timezone)
            campaign.campaign_timezone = selected_timezone[0]
            campaign.save()
            serializer = SingleCampaignSerializer(instance=campaign)
            return Response(serializer.data), campaign


class ValidateNewLeadSerializer(Serializer):
    email = fields.EmailField()
    csv_file = fields.FileField(validators=[])

    def create(self, validated_data, campaign_id=None):
        pass


class ValidateUpdateLeadSerializer(Serializer):
    firstname = fields.CharField()
    lastname = fields.CharField()
    full_name = fields.CharField()
    email = fields.EmailField()
    reviewed = fields.BooleanField(default=False)
    extra_fields = fields.JSONField()


class ValidateReviewLeadsSerializer(Serializer):
    leads = fields.CharField()

    def save(self, campaign_id):
        lead_ids = self.validated_data.get('leads')
        lead_ids = lead_ids.split(',')
        leads = Lead.objects.filter(
            id__in=lead_ids,
            campaign__campaign_id=campaign_id
        )
        if leads.exists():
            leads.update(reviewed=True)
        serializer = LeadSerializer(instance=leads, many=True)
        return Response(serializer.data)


class ValidateScheduleSerializer(Serializer):
    name = fields.CharField(max_length=100)
    start_time_at = fields.TimeField(default=datetime.time(12, 00))
    end_time_at = fields.TimeField(default=datetime.time(23, 59))
    interval = fields.IntegerField(default=1)
    sending_days = fields.JSONField()

    def save(self, campaign_id):
        try:
            campaign = Campaign.objects.get(campaign_id=campaign_id)
        except:
            raise NotFound(detail='Campaign not found')
        else:
            schedule = campaign.schedule_set.create(**self.validated_data)
            schedules = campaign.schedule_set.all()
            serializer = ScheduleSerializer(instance=schedules, many=True)
            return Response(serializer.data)
