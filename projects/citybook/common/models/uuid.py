from uuid import uuid4

from django.db import models


class UUIDmodel(models.Model):
    """
    Base model with uuid pk
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True
