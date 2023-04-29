from django.db import models


class Contact(models.Model):

    phone = models.CharField("Номер телефона", max_length=12)
    email = models.EmailField("Почта", max_length=50)

    author = models.OneToOneField("my_app.author", related_name="contacts", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self) -> str:
        return f"Контакты {self.author}"
