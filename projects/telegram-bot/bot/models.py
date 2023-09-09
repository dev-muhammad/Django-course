from django.db import models

class BotUsers(models.Model):

    id = models.CharField("Telegram ID", primary_key=True, max_length=15)
    username = models.CharField("Username", max_length=128, null=True)
    first_name = models.CharField("First Name", max_length=128, null=True)
    last_name = models.CharField("Last Name", max_length=128, null=True)
    bio = models.CharField("Bio", max_length=128, null=True)
    language_code = models.CharField("Language code", max_length=5)
    create_datetime = models.DateTimeField("Create time", auto_now_add=True)

    class Meta:
        verbose_name = "Bot user"
        verbose_name_plural = "Bot users"
    
    def __str__(self):
        return f"({self.id}) {self.username}"
