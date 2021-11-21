from django.db import models

class applicant(models.Model):
    username = models.CharField(max_length=70)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    phone_no = models.BigIntegerField()
    emailID = models.EmailField(max_length=70)
    nationality = models.CharField(max_length=70)
    
    
class institute(models.Model):
    institute_id = models.CharField(max_length=10)
    name = models.CharField(max_length=70)
    tnp_contact = models.BigIntegerField()
    students_applied = models.IntegerField()

