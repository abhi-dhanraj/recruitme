from django.core import validators
from django import forms
from django.db.models.fields import DateField
from django.forms import fields, models
from django.forms.widgets import DateInput, NumberInput, TextInput, Textarea
from .models import application
    

class Application(forms.Form):
    institute_id = forms.CharField(widget=TextInput,max_length=10,label = "Institue",help_text="eg: PICT",required=True)
    degree = forms.CharField(widget=TextInput,max_length=20,label = "Degree",required=True)
    cgpa = forms.FloatField(widget=NumberInput,label = "CGPA",required=True)
    experience = forms.CharField(widget=Textarea,label = "Experience",required=True)
    graduation_year = forms.DateField(widget=DateInput,label = "Year of Graduation",required=True)
    ans = forms.CharField(widget=Textarea,label='Why should we hire you?',required=True)

