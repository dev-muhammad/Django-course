from django.db import models


class Author(models.Model):

    first_name = models.CharField("Имя", max_length=150)
    last_name = models.CharField("Фамилия", max_length=150)
    birthdate = models.DateField("Дата рождения", null=True, blank=True)
    avatar = models.ImageField("Фотография", null=True, blank=True)
    genres = models.ManyToManyField("books.genre", related_name="authors")

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def total_books(self):
        return self.books.count()

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ["first_name"]

    def __str__(self) -> str:
        return self.fullname