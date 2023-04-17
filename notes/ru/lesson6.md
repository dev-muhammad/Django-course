## Урок 6

# Добавление моделей в админку и кастомизация вывода

## Содержание

1. Регистрация в админку
2. Поля в списке
3. Фильтрация
4. Поиск
5. Кастомные поля

---
## Регистрация модели в Django админку

Django позволяет управлять моделями созданный через Django ORM через админку. Для добавления моделей в админку необходимо регистрировать моделей в файле admin.py, который имеется в каждом приложение.

Добавляем модель Book (созданный в предыдушем уроке)
Добавим следующий код в my_app.admin.py
```
from django.contrib import admin
from my_app.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    model = Book
    list_display = ("id", "title", "author", "cover_type", "publish_year", "my_field")
    list_filter = ("publish_year", "cover_type")
    search_fields = ("title", "author")
    list_display_links = ("id", "title")
    list_per_page = 10
    date_hierarchy = "create_time"
    
    def my_field(self, instance):
        return f"Hello {instance.publish_year}"
    my_field.short_description = "Кастомное поле"
```

Создается класс регистрации модели наследовав от django.contrib.admin.ModelAdmin и через @admin.register("название модели") регистрируется в админку.

Расмотрим поля класса BookAdmin:

list_display - список полей который отображаются в общем таблице значений
list_filter - список полей по которым необходимо создавать фильтры
search_fields - список полей по которым нужно реализовать поиск
list_display_links - список полей в которых появляется ссылка для изменения объекта
list_per_page - количество объектов в каждом странице
date_hierarchy - поля с типом datetime по которому можно реализовать филтрацию

Также можно отображать кастомное поле в list_display, который продемострирован с методом my_field.

Подробнее по возможности Django админки прочитайте [тут](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/)

Откройте админку для проверки существования зарегистрированной модели и попробуйте добавить несолько записей в модель Book через админку. Изучите возможности админки.

