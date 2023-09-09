from django.db import models

from telebot import formatting


class Post(models.Model):

    title = models.CharField("Title", max_length=70)
    content = models.TextField("Content", max_length=255)
    link = models.URLField("Link", blank=True, null=True)
    #media = models.ImageField("Image", upload_to="posts")

    is_sent = models.BooleanField("Sent", default=False)
    send_time = models.DateTimeField("Send time", null=True, blank=True)
    create_time = models.DateTimeField("Create time", auto_now_add=True)

    class Meta:
            verbose_name = "Post"
            verbose_name_plural = "Posts"

    def __str__(self) -> str:
        return self.title

    def get_as_message(self) -> str:
        header = formatting.hbold(self.title)
        link = ""
        if self.link:
             link = "\n\n" + formatting.hlink("link", self.link)
        
        return f"{header} \n\n {self.content}{link}"
