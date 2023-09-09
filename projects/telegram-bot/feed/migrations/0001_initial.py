# Generated by Django 4.2 on 2023-09-09 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('content', models.CharField(max_length=255, verbose_name='Content')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('is_sent', models.BooleanField(default=False, verbose_name='Sent')),
                ('send_time', models.DateTimeField(blank=True, null=True, verbose_name='Send time')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
