import datetime
import re

import pytz
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.regex_helper import _lazy_re_compile
from django.utils.translation import gettext_lazy as _


def waiting_days_validator(value):
    if value < 1 or value > 355:
        message = 'Waiting days should be between 1 and 355 days'
        raise ValidationError(message)


def custom_id_validator(value):
    validator = RegexValidator(r'^(camp|lead|seq|sche)\_[a-zA-Z0-9]+$')
    validator(value)


def char_list_validator(sep=",", message=None, code='invalid'):
    regexp = _lazy_re_compile(
        r"^\w+(?:%(sep)s\w+)*\Z" %
        {"sep": re.escape(sep)}
    )
    return RegexValidator(regexp, message=message, code=code)


validate_comma_separated_char_list = char_list_validator(
    message=_("Enter only text separated by commas")
)
