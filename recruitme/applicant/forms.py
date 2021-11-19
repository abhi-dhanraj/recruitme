from django.core import validators
from django import forms
from .models import applicant

class Applicant(forms.ModelForm):
    class Meta:
        model = applicant
        fields = '__all__'
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            "phone_no": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone No."}),
            "emailID": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email ID"}),
            "nationality": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nationality"}),
            "institute": forms.TextInput(attrs={"class": "form-control", "placeholder": "Institute"}),
            "degree": forms.TextInput(attrs={"class": "form-control", "placeholder": "Degree"}),
            "graduation_year": forms.TextInput(attrs={"class": "form-control", "placeholder": "Graduation Year"})
        }
        labels = {'username': "", 'emailID': "",'phone_no' :"","first_name":"","last_name":"","nationality":"","graduation_year":"","institute":"","degree":""}

