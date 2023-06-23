from django.db import models


class Author(models.Model):

    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    middle_name = models.CharField("Отчество", max_length=50, blank=True, null=True)

    class Meta:
        ordering = ["first_name"]
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self) -> str:
        return self.fullname
    
    @property
    def fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

