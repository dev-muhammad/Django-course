from django.db import models


class IsActiveModel(models.Model):
    """
    Abstract model with is_active field (default True)
    """
    is_active = models.BooleanField("Активный", default=True)

    class Meta:
        abstract = True
