from django.core import validators
from django import forms
from .models import ApplicantLoggedIn, ApplicantSignedUp


# modelForm is inherited by ApplicantLogin form
class ApplicantLoginForm(forms.ModelForm):
    class Meta:
        model = ApplicantLoggedIn
        fields = ['username', 'password']
        widgets = {
            "username": forms.TextInput(attrs={"class": "input-field", "placeholder": "Username"}),
            "password": forms.PasswordInput(attrs={"class": "input-field", "placeholder": "Password"})
            # "username":forms.TextInput(attrs={"class":"className"}) //helps to give css to input text field
        }
        labels = {'username': "", 'password': ""}


class ApplicantSignUpForm(forms.ModelForm):
    class Meta:
        model = ApplicantSignedUp
        fields = ['username', 'emailID', 'newPassword']
        widgets = {
            "username": forms.TextInput(attrs={"class": "input-field", "placeholder": "Username"}),
            "emailID": forms.EmailInput(attrs={"class": "input-field", "placeholder": "Email ID"}),
            "newPassword": forms.PasswordInput(attrs={"class": "input-field", "placeholder": "Set password"})
        }
        labels = {'username': "", 'emailID': "", 'newPassword': ""}
