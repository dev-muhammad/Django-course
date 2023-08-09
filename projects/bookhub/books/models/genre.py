from django.db import models


class Genre(models.Model):

    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание", max_length=1024)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title
