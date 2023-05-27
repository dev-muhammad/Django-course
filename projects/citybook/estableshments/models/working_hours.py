from django.db import models

from .weekdays import Weekdays


class CommonWorkingHours(models.Model):

    day = models.PositiveSmallIntegerField(choices=Weekdays.choices)
    start_time = models.TimeField(default='08:00')
    end_time = models.TimeField(default='17:00')

    def __str__(self):
        return f"{self.day}: {self.start_time} to {self.end_time}"

    class Meta:
        verbose_name= 'Стандартное рабочее время'
        verbose_name_plural = 'Стандартное рабочее время'
        ordering = ['day']


class WorkingHours(models.Model):

    place = models.ForeignKey("estableshments.place", on_delete=models.CASCADE, related_name="working_hours")
    day = models.PositiveSmallIntegerField(choices=Weekdays.choices)
    start_time = models.TimeField(null=True, blank=True)
    lunch_start_time = models.TimeField(null=True, blank=True)
    lunch_end_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.place.title} {self.day}: c {self.start_time} до {self.end_time}"
    
    class Meta:
        verbose_name= 'Рабочее время'
        verbose_name_plural = 'Рабочее время'
        ordering = ['day']
