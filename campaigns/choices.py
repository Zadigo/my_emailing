import pytz


class TimeZoneChoices:
    @classmethod
    def choices(cls):
        items = []
        for timezone in pytz.all_timezones:
            human_readable = timezone.replace('/', ' - ')
            items.append((timezone, human_readable))
        return items

    @classmethod
    def choice(cls):
        return cls.choices()[0]
