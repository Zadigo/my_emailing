import datetime
import time

import pytz

SECONDS_PER_HOUR = 3600


class BaseCalendarCalcuator:
    def __init__(self, start_date, *, start_time=None, end_time=None, interval=15, leads=10, timezone='UTC'):
        if isinstance(start_date, str):
            pass

        if start_time is None:
            pass

        if end_time is None:
            pass

        self._start_date = start_date
        self._start_time = start_time
        self._end_time = end_time
        self.interval = interval
        self._leads = leads
        self.timezone = pytz.timezone(timezone)

        self.current_date = datetime.datetime.now()

        # This corresponds to the difference
        # between the start_time and the end_time
        # which gives us a window of available hours
        # in a single day in which we can send emails
        d = self.current_date.date()
        time1 = self.current_date.combine(d, self._start_time)
        time2 = self.current_date.combine(d, self._end_time)
        available_hours_per_day = (time2 - time1).total_seconds() / 3600
        # .. Converted in seconds
        seconds_per_day = SECONDS_PER_HOUR * available_hours_per_day
        # .. Converted in minutes
        minutes_per_day = seconds_per_day / 60
        # This gives us the amount of times we can actually
        # send and email using the the intervaL. For example,
        # if we have only 5h window, or 18 000s, or 300 minutes
        # and a sending interval of every 15 minutes, then it
        # means that we can send 20 times in the given day
        self.sending_number_of_times = int(
            round(minutes_per_day / interval, 0)
        )

    def __repr__(self):
        return f'<Calculator [{self.sending_number_of_times} emails/day]>'

    def __iter__(self):
        for d in self.calendar():
            yield d

    @property
    def comma_separated_calendar(self):
        return ','.join(self.calendar(as_string=True))

    def calendar(self, as_string=False):
        dates = []
        # To make a clean sending process, start sending the
        # next day as opposed to now
        next_day = datetime.timedelta(days=1) + self._start_date
        # Generate all the given available dates using
        # the interval that was provided
        for _ in range(self.sending_number_of_times):
            if len(dates) == 0:
                result = datetime.timedelta(minutes=self.interval) + next_day
            else:
                result = datetime.timedelta(minutes=self.interval) + dates[-1]

            dates.append(result)

        if as_string:
            return [str(d) for d in dates]
        return dates


class CalendarCalculator(BaseCalendarCalcuator):
    def __init__(self, instance):
        super().__init__(
            instance.campaign.start_date,
            start_time=instance.start_time_at,
            end_time=instance.end_time_at,
            interval=instance.interval,
            leads=instance.campaign.number_of_leads,
            timezone='UTC'
        )
        self.instance = instance
