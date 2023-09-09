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
    def choice(cls, value=None):
        if value is not None:
            result = list(filter(lambda x: value in x, cls.choices()))
            return result[0]
        return cls.choices()[0]
