from django import forms
from django.core.validators import MinValueValidator

from .models import Customer, Owner, Employee

secrets = {
    "employee": "employee_secret_code",
}


class CustomerForm(forms.ModelForm):
    budget = forms.DecimalField(
        validators=[MinValueValidator(0)],
        help_text="Budget must be positive"
    )
    class Meta:
        model = Customer
        fields = ["budget", "notes"]
        widgets = {
            "notes": forms.Textarea(attrs={"rows": 4, "placeholder": "Leave some notes about yourself..."}),
        }


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ["preferred_contact_time", "notes"]
        widgets = {
            "notes": forms.Textarea(attrs={"rows": 4, "placeholder": "Leave some notes about yourself..."}),
        }


class EmployeeForm(forms.ModelForm):
    work_experience = forms.DecimalField(
        validators=[MinValueValidator(0)],
        help_text="Work experience must be positive"
    )
    secret_code = forms.CharField(
        help_text="The confirmation code that you are an employee",
        max_length=20
    )
    class Meta:
        model = Employee
        fields = ["work_type", "work_experience", "image"]
        widgets = {
           "work_type": forms.Select(),
        }

    def clean_secret_code(self):
        secret_code = self.cleaned_data['secret_code']
        if secret_code != secrets["employee"]:
            raise forms.ValidationError("Secret codes mismatches. You are not employee")
        return secret_code