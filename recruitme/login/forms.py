from django.core import validators
from django import forms
from .models import ApplicantCredentials


# modelForm is inherited by ApplicantLogin form
class ApplicantLoginForm(forms.ModelForm):
    class Meta:
        model = ApplicantCredentials
        fields = ['username', 'password']
        widgets = {
            "username": forms.TextInput(attrs={"class": "input-field", "placeholder": "Username"}),
            "password": forms.PasswordInput(attrs={"class": "input-field", "placeholder": "Password"})
            # "username":forms.TextInput(attrs={"class":"className"}) //helps to give css to input text field
        }
        labels = {'username': "", 'password': ""}
