from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator
from applicant.models import applicant, institute
from jobs.models import jobs
# Create your models here.
class rounds(models.Model):
    aptitude = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    interview = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    professional_fitment    = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    hr = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    stage = models.IntegerField(validators=[
            MaxValueValidator(4),
            MinValueValidator(0)
        ])
    total_points= models.IntegerField(validators=[
            MaxValueValidator(400),
            MinValueValidator(0)
        ])


class process(models.Model):
    status = models.BooleanField()
    round_id = models.ForeignKey(rounds,on_delete=CASCADE)

class application(models.Model):
    applicant_id = models.ForeignKey(applicant,on_delete = CASCADE,null=True);
    process_id = models.ForeignKey(process,on_delete=CASCADE,null=True)
    job_id = models.ForeignKey(jobs,on_delete=CASCADE,null=True)
    institute_id = models.ForeignKey(institute,on_delete = CASCADE,null=True)
    degree = models.CharField(max_length=70,null=True)
    graduation_year = models.DateField(null=True)
    cgpa = models.FloatField(default = 0.0,validators=[
            MaxValueValidator(10.0),
            MinValueValidator(0.0)
        ])
    experience = models.TextField(null=True)
    date_of_application = models.DateField(null=True)
    ans = models.TextField(null=True)







