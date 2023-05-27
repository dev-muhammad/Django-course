from django.db import models


class Photo(models.Model):
    place = models.ForeignKey("estableshments.place", on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to='photos/place/')
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name= 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['order']
