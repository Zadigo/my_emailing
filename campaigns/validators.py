import datetime
import re
from django.conf import settings
import pytz
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone


def waiting_days_validator(value):
    if value < 1 or value > 355:
        message = 'Waiting days should be between 1 and 355 days'
        raise ValidationError(message)


def custom_id_validator(value):
    validator = RegexValidator(r'^(camp|lead|seq)\_[a-zA-Z0-9]+$')
    validator(value)
