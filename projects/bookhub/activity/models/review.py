from django.db import models
from django.conf import settings


class Review(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    book = models.ForeignKey("books.book", on_delete=models.CASCADE, related_name="reviews")
    rate = models.PositiveSmallIntegerField("Оценка", default=5)
    description = models.TextField("Отзыв", max_length=1024)
    create_time = models.DateTimeField("Время создания", auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-create_time"]
    
    def __str__(self) -> str:
        return f"{self.user} - {self.book} ({self.rate})"

