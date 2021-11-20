from django.db import models

# Create your models here.


class jobs(models.Model):
    job_id = models.IntegerField()
    title = models.CharField(max_length=70)
    vacancies = models.IntegerField()
    jobs_position = models.CharField(max_length=70)
    jobs_category = models.CharField(max_length=70)
    description = models.TextField()
    apply_by_date = models.DateField()
    start_date = models.DateField()
    contact = models.BigIntegerField()
    salary = models.BigIntegerField()
    workplace = models.CharField(max_length=70)
