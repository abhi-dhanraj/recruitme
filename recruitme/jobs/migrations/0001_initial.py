# Generated by Django 3.2.7 on 2021-11-20 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.IntegerField()),
                ('title', models.CharField(max_length=70)),
                ('vacancies', models.IntegerField()),
                ('jobs_position', models.CharField(max_length=70)),
                ('jobs_category', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('apply_by_date', models.DateField()),
                ('start_date', models.DateField()),
                ('contact', models.BigIntegerField()),
                ('salary', models.BigIntegerField()),
                ('workplace', models.CharField(max_length=70)),
            ],
        ),
    ]
