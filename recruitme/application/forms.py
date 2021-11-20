from django.core import validators
from django import forms
from django.forms import fields, models
from .models import application

class Application(forms.ModelForm):
    class Meta:
        model = application
        fields = ['degree','cgpa','experience','graduation_year']
        widgets = {
            "degree": forms.TextInput(attrs={"class": "form-control", "placeholder": "Degree"}),
            "cgpa": forms.TextInput(attrs={"class": "form-control", "placeholder": "CGPA"}),
            "experience": forms.TextInput(attrs={"class": "form-control", "placeholder": "Experience"}),
            "graduation_year": forms.TextInput(attrs={"class": "form-control", "placeholder": "Year of Graduation"}),
        }
        labels = {"graduation_year":"","cgpa":"","degree":"","experience":""}
        

