# Generated by Django 4.1.1 on 2022-11-08 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accreditation_app', '0021_institute_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institute_details',
            name='emp',
        ),
    ]
