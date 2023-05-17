from django.db import models


class BookManager(models.Manager):

    def get_pushkin(self):
        return super().filter(author__first_name__icontains = "Пушкин")

    def get_by_author_name(self, author_name):
        return super().filter(author__first_name__icontains = author_name)


class PushkinManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(author__first_name__icontains = "Пушкин")


class PushkinQuerySet(models.QuerySet):
    def books(self):
        return self.filter(author__first_name__icontains = "Пушкин")


class Book(models.Model):

    title = models.CharField("Название", max_length=120)
    # author = models.CharField("Автор", max_length=120)
    
    author = models.ForeignKey("my_app.author", on_delete=models.CASCADE, related_name="books", verbose_name="Автор", null=True)

    categories = models.ManyToManyField("my_app.category", verbose_name="Категории")

    cover_type = models.CharField("Тип переплета", 
                                  max_length=25,
                                  default="Paper",
                                  )
    publish_year = models.IntegerField("Год публикации", 
                                       blank=True, null=True)
    create_time = models.DateTimeField("Дата создания", 
                                       auto_now_add=True)
    update_time = models.DateTimeField("Дата обновления",
                                       auto_now=True)

    objects = BookManager()
    pushkin = PushkinManager()
    pushkin1 = PushkinQuerySet.as_manager()

    class Meta:
        ordering = ["title"]
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self) -> str:
        return self.title
      