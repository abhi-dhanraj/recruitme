# Generated by Django 3.2.7 on 2021-11-20 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0003_institue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='graduation_year',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='institute',
        ),
    ]
