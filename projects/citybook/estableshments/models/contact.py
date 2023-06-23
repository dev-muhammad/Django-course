from django.db import models


class Contact(models.Model):

    place = models.OneToOneField("estableshments.place", on_delete=models.CASCADE, related_name="contacts")
    primary_phone = models.CharField(max_length=12)
    secondary_phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=120)
    website = models.URLField(max_length=120)

    def __str__(self):
        return f"{self.primary_phone}"

    class Meta:
        verbose_name= 'Контакт'
        verbose_name_plural = 'Контакты'
