import datetime
import time
import pytz


class CalendarCalculator:
    def __init__(self, start_date, *, start_time=None, end_time=None, interval=15, leads=10, timezone='UTC'):
        self.timezone = pytz.timezone(timezone)
        self.interval = interval
        self.start_date = None
        if isinstance(start_date, str):
            start_date = datetime.datetime.strptime(
                start_date,
                '%Y-%m-%d %H:%M:%S.%f%z'
            )
            try:
                self.start_date = self.timezone.localize(start_date)
            except ValueError:
                self.start_date = start_date

        current_date = datetime.datetime.now()
        time_params = {
            'year': current_date.year,
            'month': current_date.month,
            'day': current_date.day,
            'hour': 6,
            'second': 0

        }
        if start_time is None:
            # No start time means that the whole clock
            # is used e.g. from 6:00 to 18:00
            start_time = datetime.datetime(**time_params)

        if end_time is None:
            # time_params.update(hour=18)
            end_time = datetime.datetime(**time_params).replace(hour=18)

        print(end_time - start_time)

        seconds_per_hour = 3600
        hours_per_day = 5
        # hours_per_day = (end_time - start_time)
        # print(hours_per_day)
        seconds_per_day = seconds_per_hour * hours_per_day
        minutes_per_day = seconds_per_day / 60
        number_of_interval_per_day = minutes_per_day / interval
        self.number_of_interval_per_day = number_of_interval_per_day
        print(number_of_interval_per_day)

    def generate_calendar(self):
        sending_calendar = []
        for _ in range(int(self.number_of_interval_per_day)):
            if len(sending_calendar) == 0:
                sending_calendar.append(
                    datetime.timedelta(minutes=self.interval) +
                    self.start_date
                )
            else:
                sending_calendar.append(
                    datetime.timedelta(minutes=self.interval) +
                    sending_calendar[-1]
                )
        return sending_calendar


c = CalendarCalculator('2023-09-09 22:34:08.437907+00:00')
# print(c.generate_calendar())
