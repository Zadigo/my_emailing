import datetime
from django.utils.crypto import get_random_string
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from campaigns.choices import TimeZoneChoices
import pytz

class Sequence(models.Model):
    campaign = models.ForeignKey(
        'Campaign',
        on_delete=models.CASCADE
    )
    sequence_id = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    number_of_days = models.PositiveIntegerField(
        default=1,
        validators=[],
        help_text='Number of days before sending the email'
    )
    email_object = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    email_text = models.TextField(
        max_length=5000,
        blank=True,
        null=True
    )
    html_text = models.TextField(
        max_length=20000,
        blank=True,
        null=True
    )
    modified_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Sequence for {self.campaign.id}'

    @property
    def get_vue_absolute_url(self):
        return f"/{self.campaign.campaign_id}/{self.sequence_id}"


class Lead(models.Model):
    campaign = models.ForeignKey(
        'Campaign',
        on_delete=models.CASCADE
    )
    firstname = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    lastname = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    email = models.EmailField(
        blank=True,
        null=True
    )
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Lead for {self.campaign.id}'

    @property
    def full_name(self):
        return f'{self.firstname} {self.lastname}'

    def clean(self):
        if self.completed:
            self.completion_date = timezone.make_aware(
                datetime.datetime.now(),
                pytz.timezone(self.campaign.campaign_timezone)
            )


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    sender = models.EmailField(blank=True, null=True)
    team = None
    campaign_id = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    campaign_timezone = models.CharField(
        max_length=100,
        default=TimeZoneChoices.choice(),
        choices=TimeZoneChoices.choices()
    )
    debut_sending_time = None
    end_sending_time = None
    start_date = models.DateTimeField(default=timezone.now)
    archived = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    modified_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Campaign {self.pk}'

    @property
    def get_vue_absolute_url(self):
        return f"/{self.campaign_id}"

    @property
    def number_of_leads(self):
        return self.lead_set.count()

    def clean(self):
        if self.active:
            print(self.start_date)
            self.start_date = timezone.make_aware(
                datetime.datetime.now(),
                pytz.timezone(self.campaign_timezone)
            )


@receiver(post_save, sender=Campaign)
def create_campaign_id(instance, created, **kwargs):
    if created:
        if instance.campaign_id is None:
            secret = get_random_string(length=8)
            instance.campaign_id = f'camp_{secret}'
            instance.save()


@receiver(post_save, sender=Sequence)
def create_sequence_id(instance, created, **kwargs):
    if created:
        if instance.campaign_id is None:
            secret = get_random_string(length=8)
            instance.campaign_id = f'seq_{secret}'
            instance.save()
