from django.db import models


class TitleDescriptionModel(models.Model):
    """
    Abstact model with title and description field
    """
    title = models.CharField("Заголовок", max_length=70)
    description = models.TextField("Описание", max_length=512, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        abstract = True
