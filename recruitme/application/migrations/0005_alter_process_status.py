# Generated by Django 3.2.7 on 2021-11-21 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_process_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='status',
            field=models.IntegerField(),
        ),
    ]