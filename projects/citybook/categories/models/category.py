from django.db import models

from common.models import BaseInfoModel


class Category(BaseInfoModel):
    """
    Category model
    fields:
        - id (uuid)
        - create_time (datetime)
        - update_time (datetime)
        - is_active (bool defaul=True)
        - title
        - description
        - parent (fk self)
    """
    parent = models.ForeignKey("self", 
                               on_delete=models.CASCADE, 
                               blank=True, 
                               null=True,
                               related_name="subcategories", 
                               verbose_name="Родительская категория")

    class Meta:
        verbose_name= 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']