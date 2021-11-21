# Generated by Django 3.2.7 on 2021-11-20 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0002_rename_insititue_applicant_institute'),
    ]

    operations = [
        migrations.CreateModel(
            name='institue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institue_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=70)),
                ('tnp_contact', models.BigIntegerField()),
                ('students_applied', models.IntegerField()),
            ],
        ),
    ]
