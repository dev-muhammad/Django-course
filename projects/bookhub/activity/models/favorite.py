from django.db import models
from django.conf import settings


class Favorite(models.Model):

    class Status(models.TextChoices):
        WANT2READ = "WANT2READ", "Хочу читать"
        READING = "READING", "Читаю"
        READ = "READ", "Прочитал"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favorites")
    book = models.ForeignKey("books.book", on_delete=models.CASCADE, related_name="favorites")
    status = models.CharField("Статус", choices=Status.choices, default=Status.WANT2READ, max_length=20)
    create_time = models.DateTimeField("Время создания", auto_now_add=True)

    class Meta:
        verbose_name = "Избранный"
        verbose_name_plural = "Избранные"
        ordering = ["-create_time"]

    def __str__(self) -> str:
        return f"{self.user} - {self.book} ({self.status})"
