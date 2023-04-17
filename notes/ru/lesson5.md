## Урок 5

# Создание моделей данных в Django

## Содержание

1. Django ORM модель
2. Типы полей
3. Связи между моделей
4. CRUD
5. Менеджер моделей

---
## Создание нового приложения в Django

Для начало создаем новое приложение в проекте Django (если у вас еще нет инициализированного Django проекта, сперва вам нужно сделать это)

```
python manage.py startapp my_app
```

my_app это название приложения. Данное приложение необходимо добавить в список INSTALLED_APPS в модуле settings.py основного проекта. INSTALLED_APPS должно выглядеть вот так:

```
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "my_app", # <-- название нашего приложения
]
```

## Создание моделя 

В Django ORM каждая таблица это python класс наследовавший от django.db.models.Model, а поля таблицы - свойства класса. 

Создаем объект Book в файле my_app.models.py:

```
from django.db import models


class Book(models.Model):

    title = models.CharField("Название", max_length=120)
    author = models.CharField("Автор", max_length=120)
    cover_type = models.CharField("Тип переплета", max_length=25, default="Paper")
    publish_year = models.IntegerField("Год публикации", blank=True, null=True)
    create_time = models.DateTimeField("Дата создания", auto_now_add=True)
    update_time = models.DateTimeField("Дата обновления", auto_now=True)
``` 

В свойствах класс добавляем название полей и задаём их типы данных и соответсвующее параметры.
Подробнее о типах полей и их параметров можете прочитать в документации [Django](https://docs.djangoproject.com/en/4.2/topics/db/models/)

## Meta класс моделей

Через мета класс можем задавать дополнительные параметры для моделей, как название модели, поле сортировки по умолчанию и т.д.

Добавляем мета класс в модель Book

```
class Book(models.Model):

    title = models.CharField("Название", max_length=120)
    author = models.CharField("Автор", max_length=120)
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

    class Meta:
        ordering = ["title"]
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
```

Подробнее о мета классе причитайте [тут](https://docs.djangoproject.com/en/4.2/ref/models/options/)

## Добавление модели в базу данных

После создание модели нужно добавить в базу. Каждая модель будет добавлен в базу в виде таблицы.
Сперва нужно создать файлы миграции:
```
python manage.py makemigrations
```

Потом применяем миграцию в базу:
```
python manage.py migrate
```

После этих команд наш модель появляется в базе и можем добавлять, изменить и удалить данных с базы по ORM.

Возможности ORM рассмотрим в следующих уроках.
