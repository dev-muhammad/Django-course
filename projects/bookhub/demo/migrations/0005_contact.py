# Generated by Django 4.2.2 on 2023-07-29 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("demo", "0004_category_book_categories"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("phone", models.CharField(max_length=12, verbose_name="Телефон")),
                ("email", models.EmailField(max_length=254, verbose_name="Эл.почта")),
                (
                    "telegram",
                    models.URLField(blank=True, null=True, verbose_name="Телеграм"),
                ),
                (
                    "author",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contacts",
                        to="demo.author",
                    ),
                ),
            ],
            options={
                "verbose_name": "Контакт",
                "verbose_name_plural": "Контакты",
                "ordering": ["author"],
            },
        ),
    ]
