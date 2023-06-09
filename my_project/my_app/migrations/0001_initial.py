# Generated by Django 4.2 on 2023-04-15 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=120, verbose_name="Название")),
                ("author", models.CharField(max_length=120, verbose_name="Автор")),
                (
                    "cover_type",
                    models.CharField(max_length=25, verbose_name="Тип переплета"),
                ),
                ("publish_year", models.IntegerField(verbose_name="Год публикации")),
            ],
            options={
                "verbose_name": "Книга",
                "verbose_name_plural": "Книги",
                "ordering": ["title"],
            },
        ),
    ]
