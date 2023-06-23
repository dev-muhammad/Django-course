from django.db import models


class CreateUpdatetimeModel(models.Model):
    """
    Abstact model with create and update time ordered by create time
    """
    create_time = models.DateTimeField("Время создания", auto_now_add=True)
    update_time = models.DateTimeField("Время изменения", auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-create_time']
