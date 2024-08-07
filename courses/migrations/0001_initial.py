# Generated by Django 5.0.7 on 2024-08-01 00:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                (
                    "name",
                    models.CharField(
                        help_text="Введите название курса",
                        max_length=100,
                        verbose_name="Название курса",
                    ),
                ),
                (
                    "preview_course",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите превью(картинку) курса",
                        null=True,
                        upload_to="courses/preview_course",
                        verbose_name="Превью курса",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Укажите описание курса",
                        null=True,
                        verbose_name="Описание курса",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
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
                (
                    "name",
                    models.CharField(
                        help_text="Введите название урока",
                        max_length=100,
                        verbose_name="Название урока",
                    ),
                ),
                (
                    "preview_lesson",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите превью(картинку) урока",
                        null=True,
                        upload_to="lessons/preview_lesson",
                        verbose_name="Превью урока",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Укажите описание урока",
                        null=True,
                        verbose_name="Описание урока",
                    ),
                ),
                (
                    "link_to_video",
                    models.CharField(
                        blank=True,
                        help_text="Укажите ссылку",
                        max_length=100,
                        null=True,
                        verbose_name="Ссылка на видео",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        help_text="Выберите курс",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="courses.course",
                        verbose_name="Курс",
                    ),
                ),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
            },
        ),
    ]
