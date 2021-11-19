from django.db import models

class applicant(models.Model):
    username = models.CharField(max_length=70)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    phone_no = models.BigIntegerField()
    emailID = models.EmailField(max_length=70)
    nationality = models.CharField(max_length=70)
    institute = models.CharField(max_length=70)
    degree = models.CharField(max_length=70)
    graduation_year = models.DateField()
    