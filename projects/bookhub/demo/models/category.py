from django.db import models


class Category(models.Model):

    name = models.CharField("Название", max_length=50)
    description = models.TextField("Описание", max_length=512)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name
