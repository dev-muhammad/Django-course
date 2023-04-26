from django.db import models


class Category(models.Model):

    title = models.CharField("Название", max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.title
