from django.db import models

from common.models import BaseInfoModel


class City(BaseInfoModel):
    """
    City model
    fields:
        - id (uuid)
        - create_time (datetime)
        - update_time (datetime)
        - is_active (bool defaul=True)
        - title
        - description
        - country (fk locations.country)
    """

    country = models.ForeignKey("locations.country", 
                            on_delete=models.CASCADE, 
                            blank=True, 
                            null=True,
                            related_name="cites", 
                            verbose_name="Страна")


    class Meta:
        verbose_name= 'Город'
        verbose_name_plural = 'Города'
