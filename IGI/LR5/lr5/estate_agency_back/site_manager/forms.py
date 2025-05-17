import datetime
import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as DjangoUser
from django.core.exceptions import ValidationError

from estate_agency.models import User


def phone_num_validator(value):
    if not re.match(r"^\+375(:?33|29|25|44)\d{7}$", value):
        raise ValidationError("Enter correct phone num")


def birth_date_validator(value : datetime.date):
    today = datetime.date.today()
    today_18_years_ago = datetime.date(today.year - 18, today.month, today.day)
    today_100_years_ago = datetime.date(today.year - 100, today.month, today.day)
    if value > today_18_years_ago:
        raise ValidationError("You must be at least 18 years old.")
    if value >= datetime.date.today() or value < today_100_years_ago:
        raise ValidationError("Incorrect date ")



class CustomRegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=80, label="Full Name", required=True)
    phone_number = forms.CharField(required=False, label="Phone Number")
    email = forms.EmailField(label="Email")
    birth_date = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

    class Meta:
        model = DjangoUser
        fields = ["username", "password1", "password2", "email"]

    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone_number")
        if phone:
            phone_num_validator(phone)
        return phone

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get("birth_date")
        if birth_date:
            birth_date_validator(birth_date)
        return birth_date

    def save(self, commit=True):
        user = super().save(commit=commit)
        try:
           User.objects.create(
                user=user,
                full_name=self.cleaned_data["full_name"],
                birth_day=self.cleaned_data["birth_date"],
                phone_number=self.cleaned_data["phone_number"],
                email=self.cleaned_data["email"]
            )
        except ValidationError:
            user.delete()
        return user


