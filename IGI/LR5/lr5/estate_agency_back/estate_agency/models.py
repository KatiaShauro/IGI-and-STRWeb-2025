import datetime
from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, RegexValidator
from django.db import models


phone_num_validator = RegexValidator(r"^\+375(:?33|29|25|44)\d{7}$")


class TypeOfWork(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        verbose_name="Work type name",
        help_text="Вид работы",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Work description",
        help_text="Описание работы",
    )

    def __str__(self):
        return self.name


class User(models.Model):
    full_name = models.CharField(
        blank=False,
        null=False,
        verbose_name="Full ame",
        help_text="ФИО",
        max_length=80
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Employee(models.Model, User):
    work_type = models.ForeignKey("TypeOfWork", on_delete=models.PROTECT, null=True)
    work_experience = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Work experience",
        help_text="Трудовой опыт",
        validators=[MinValueValidator(0),
                    MaxValueValidator(70)]
    )


class Owner(models.Model, User):
    rating = models.FloatField(
        default=0.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        help_text="Рейтинг владельца от 0 до 5"
    )
    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Дополнительная информация о владельце"
    )
    phone_number = models.TextField(
        blank=False,
        null=False,
        verbose_name="Phone number",
        help_text="Телефон",
        validators=[phone_num_validator]
    )
    preferred_contact_time = models.CharField(
        max_length=50,
        blank=True,
        help_text="Предпочтительное время связи"
    )

    def __str__(self):
        return (f"Name: {self.full_name}\n"
                f"Work experience: {self.work_experience}")


class Customer(models.Model, User):
    budget = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Максимальный бюджет клиента"
    )
    is_vip = models.BooleanField(
        default=False,
        verbose_name="VIP клиент"
    )
    notes = models.TextField(
        blank=True,
        help_text="Дополнительная информация о клиенте"
    )


class RealtyType(models.Model):
    class RealtyCategory(models.TextChoices):
        RESIDENTIAL = "RES", "Жилая"
        COMMERCIAL = "COM", "Коммерческая"
        LAND = "LAND", "Земельный участок"
        OTHER = "OTH", "Другое"

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Type name",
        help_text="Пример: квартира, дом, офис",
        validators=[MinLengthValidator(2)]
    )
    category = models.CharField(
        max_length=4,
        choices=RealtyCategory.choices,
        default=RealtyCategory.RESIDENTIAL,
        verbose_name="Category"
    )

    def __str__(self):
        return f"{self.name}, {self.category}"


class Realty(models.Model):
    type = models.ForeignKey("RealtyType", on_delete=models.PROTECT, null=False)
    owner = models.ForeignKey("Owner", on_delete=models.CASCADE, null=False)
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Realty name",
        help_text="Наименование недвижимости",
        validators=[MinLengthValidator(5)]
    )
    address = models.CharField(
        max_length=100,
        verbose_name="Address",
        help_text="Адрес",
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
        help_text="Цена в валюте"
    )
    area = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
        help_text="Общая площадь в м²"
    )
    built_year = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        help_text="Год постройки",
        validators=[MinValueValidator(1800),
                    MaxValueValidator(datetime.datetime.now().year)]
    )

    def __str__(self):
        return f"{self.name} for {self.price}"


class Deal(models.Model):
    class DealType(models.TextChoices):
        SALE = "SALE", "Продажа"
        RENT = "RENT", "Аренда"
        EXCHANGE = "EXCHANGE", "Обмен"

    class DealStatus(models.TextChoices):
        DRAFT = "DRAFT", "Черновик"
        ACTIVE = "ACTIVE", "В процессе"
        COMPLETED = "COMPLETED", "Завершена"
        CANCELLED = "CANCELLED", "Отменена"
        SUSPENDED = "SUSPENDED", "Приостановлена"

    deal_type = models.CharField(
        max_length=10,
        choices=DealType.choices,
    )
    status = models.CharField(
        max_length=10,
        choices=DealStatus.choices,
        default=DealStatus.DRAFT,
    )
    realty = models.ForeignKey(
        "Realty",
        on_delete=models.PROTECT,
        related_name="deals",
        help_text="Объект недвижимости"
    )
    customer = models.ForeignKey(
        "Customer",
        on_delete=models.PROTECT,
        related_name="deals",
    )
    owner = models.ForeignKey(
        "Owner",
        on_delete=models.PROTECT,
    )
    actual_end_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="End of payment",
        help_text="Фактическая дата завершения платежей"
    )
