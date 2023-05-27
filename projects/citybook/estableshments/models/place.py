from django.db import models

from common.models import BaseInfoModel


class Place(BaseInfoModel):

    category = models.ForeignKey("categories.category", on_delete=models.CASCADE)
    address = models.CharField(max_length=70)
    city = models.ForeignKey("locations.city", on_delete=models.CASCADE, related_name="places")

    class Meta:
        verbose_name= 'Заведение'
        verbose_name_plural = 'Заведения'
        ordering = ['title']
