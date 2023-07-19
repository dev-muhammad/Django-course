from django.db import models


class Book(models.Model):

    name = models.CharField("Название", max_length=100)
    author = models.CharField("Автор", max_length=50)
    publish_year = models.IntegerField("Год издания")
    publisher = models.CharField("Издательство", max_length=50)
    description = models.TextField("Описание", null=True, blank=True)
    pages = models.PositiveIntegerField("Количество страниц")
    is_active = models.BooleanField("Есть в наличие", default=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name
