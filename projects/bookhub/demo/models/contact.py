from django.db import models


class Contact(models.Model):

    author = models.OneToOneField("demo.author", on_delete=models.CASCADE, related_name="contacts")

    phone = models.CharField("Телефон", max_length=12)
    email = models.EmailField("Эл.почта")
    telegram = models.URLField("Телеграм", null=True, blank=True)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ['author']
    
    def __str__(self) -> str:
        return f"Контакты {self.author}"
