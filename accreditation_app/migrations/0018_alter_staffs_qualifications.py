# Generated by Django 4.0.4 on 2022-07-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accreditation_app', '0017_alter_ta_guide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffs',
            name='qualifications',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
