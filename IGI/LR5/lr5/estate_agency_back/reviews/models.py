from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from estate_agency.models import User


class Review(models.Model):
    title = models.CharField(
        blank=False,
        null=False,
        verbose_name="Review title",
        max_length=60,
        validators=[MinLengthValidator(5)],
        help_text="Заголовок отзыва"
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(
        blank=True,
        null=True,
        verbose_name="Review content",
        validators=[MinLengthValidator(5)],
        help_text="Содержание отзыва"
    )
    rate = models.FloatField(
        null=False,
        blank=False,
        verbose_name="Rating",
        help_text="Оценка",
        validators=[MinValueValidator(0),
                    MaxValueValidator(10)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review '{self.title}', rate {self.rate}"
