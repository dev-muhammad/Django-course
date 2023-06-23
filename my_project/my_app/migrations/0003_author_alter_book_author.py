# Generated by Django 4.2 on 2023-04-26 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("my_app", "0002_book_create_time_book_update_time_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("first_name", models.CharField(max_length=50, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=50, verbose_name="Фамилия")),
                (
                    "middle_name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Отчество"
                    ),
                ),
            ],
            options={
                "verbose_name": "Автор",
                "verbose_name_plural": "Авторы",
                "ordering": ["first_name"],
            },
        ),
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="books",
                to="my_app.author",
                verbose_name="Автор",
            ),
        ),
    ]
