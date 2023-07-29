from django.db import models


class Author(models.Model):
    """
    Author model
    """
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    birthdate = models.DateField("Дата рождения")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ['first_name', 'last_name']
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name[0]}."
    
    @property
    def total_books(self):
        return self.books.count()

