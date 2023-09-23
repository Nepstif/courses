from django.contrib.auth.models import User
from django.db import models

import product
from app.base.models import TimeStampMixin
from product.models import Product


class Lesson(TimeStampMixin):
    """Модель урока."""

    name = models.CharField(
        max_length=255,
        verbose_name="Название урока"
    )

    video = models.URLField(
        verbose_name="Видео урока"
    )

    duration = models.IntegerField(
        verbose_name="Продолжительность"
    )

    product = models.ManyToManyField(
        Product,
        related_name='products'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["name"]


class LessonViewer(TimeStampMixin):
    """Модель  для хранения данных о просмотрах лекций"""

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Пользователь",
        related_name='users',

    )

    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.PROTECT,
        verbose_name="Урок",
        related_name='lessons',
    )

    viewed_time = models.IntegerField(
        verbose_name="Время просмотра видео в секундах"
    )

    viewed = models.BooleanField(
        default=False,
        verbose_name="Статус просмотра видео"
    )

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if (self.viewed_time / self.lesson.duration) >= 0.8:
            self.viewed = True
        super().save()

    class Meta:
        verbose_name = "Просмотр урока"
        verbose_name_plural = "Просмотр уроков"
        ordering = ["user"]