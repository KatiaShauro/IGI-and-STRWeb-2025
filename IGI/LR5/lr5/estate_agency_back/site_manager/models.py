from django.db import models
from django.core.validators import RegexValidator

from estate_agency.models import TypeOfWork, Employee


phone_num_validator = RegexValidator(r"^\+375(:?33|29|25|44)\d{7}$")


class AboutCompany(models.Model):
    video = models.URLField(
        unique=True,
        blank=True,
        null=True,
        verbose_name="Video",
        help_text="Ссылка на видео (YouTube, Vimeo и т.д.)"
    )
    logo = models.ImageField(
        unique=True,
        blank=True,
        null=True,
        verbose_name="Logo",
        help_text="Логотип компании",
        upload_to='company_logos/'
    )
    history = models.TextField(
        null=True,
        verbose_name="Logo",
        help_text="История компании",
    )
    requisites = models.TextField(
        null=True,
        verbose_name="Requisites",
        help_text="Реквизиты компании",
    )

    def __str__(self):
        return (f"About company info:\n"
                f"\tVideo url: {self.video}\n"
                f"\tRequisites: {self.requisites}")


class FAQ(models.Model):
    question = models.CharField(max_length=120)
    answer = models.CharField(max_length=500)
    answer_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"Q: {self.question}\n"
                f"A: {self.answer}")

class Contacts(models.Model):
    image = models.ImageField(
        blank=True,
        null=True,
        verbose_name="Employee image",
        help_text="Фото сотрудника",
        upload_to='employee_images/'
    )
    employee = models.OneToOneField("Employee", on_delete=models.CASCADE)
    phone_number = models.TextField(
        blank=False,
        null=False,
        verbose_name="Phone number",
        help_text="Телефон",
        validators=[phone_num_validator]
    )
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        verbose_name="Email",
        help_text="Почта",
    )

    def __str__(self):
        return (f"Name: {self.employee.full_name}\n"
                f"Phone: {self.phone_number}"
                f"Email: {self.email}"
                )


class PrivacyPolicy(models.Model):
    policy_content = models.TextField()

    def __str__(self):
        return f"Privacy policy: {self.policy_content}"


class Vacancy(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    work_type = models.ForeignKey(
        "TypeOfWork",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title