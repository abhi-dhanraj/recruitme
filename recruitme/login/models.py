from django.db import models

# Create your models here.


class ApplicantLoggedIn(models.Model):
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=50)


class ApplicantSignedUp(models.Model):
    username = models.CharField(max_length=70)
    emailID = models.EmailField(max_length=70)
    newPassword = models.CharField(max_length=50)
