from django.core import validators
from django import forms
from .models import ApplicantCredentials


# modelForm is inherited by ApplicantLogin form
class ApplicantLoginForm(forms.ModelForm):
    class Meta:
        model = ApplicantCredentials
        fields = ['username', 'password']
        widgets = {
            "password": forms.PasswordInput(attrs={"placeholder": "Enter Password"}),
            "username": forms.TextInput(attrs={"placeholder": "Enter Username"})
            # "username":forms.TextInput(attrs={"class":"className"}) //helps to give css to input text field
        }
        #labels = {'username': "Enter username", 'password': "Enter password"}
