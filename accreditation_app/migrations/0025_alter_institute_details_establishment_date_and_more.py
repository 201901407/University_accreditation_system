# Generated by Django 4.1.1 on 2022-11-08 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accreditation_app', '0024_alter_institute_details_establishment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute_details',
            name='establishment_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='institute_details',
            name='recognition_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
