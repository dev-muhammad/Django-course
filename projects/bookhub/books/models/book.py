from django.db import models
from django.db.models.aggregates import Avg

class Book(models.Model):

    title = models.CharField("Название", max_length=150)
    publish_year = models.PositiveSmallIntegerField("Год издания", null=True, blank=True)
    genre = models.ForeignKey("books.genre", related_name="books", on_delete=models.CASCADE)
    author = models.ForeignKey("books.author", related_name="books", on_delete=models.CASCADE)
    pages_count = models.PositiveSmallIntegerField("Количество страниц", null=True, blank=True)
    description = models.TextField("Краткое описание", max_length=1024)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title