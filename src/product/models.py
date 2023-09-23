from django.contrib.auth.models import User
from django.db import models

from app.base.models import TimeStampMixin

class Product(TimeStampMixin):
    """Модель продукта."""

    name = models.CharField(
        max_length=255,
        verbose_name="Название продукта"
    )

    description = models.CharField(
        max_length=255,
        verbose_name="Описание",
        help_text="Краткое описание продукта",
    )

    access = models.BooleanField(
        default=False
    )

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='user',

    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]

