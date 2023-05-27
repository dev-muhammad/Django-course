from django.db import models


class GpsLocation(models.Model):

    place = models.OneToOneField("estableshments.place", on_delete=models.CASCADE, related_name="gps_location")
    lat = models.FloatField()
    lon = models.FloatField()
