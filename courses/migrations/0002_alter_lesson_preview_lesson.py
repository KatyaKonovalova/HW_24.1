# Generated by Django 5.0.7 on 2024-08-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="preview_lesson",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите превью(картинку) урока",
                null=True,
                upload_to="courses/preview_lesson",
                verbose_name="Превью урока",
            ),
        ),
    ]
