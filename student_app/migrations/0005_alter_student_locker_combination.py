# Generated by Django 4.2.7 on 2023-11-27 00:04

from django.db import migrations, models
import student_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0004_alter_student_locker_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='locker_combination',
            field=models.CharField(default='12-12-12', max_length=8, validators=[student_app.validators.validate_locker_combination]),
        ),
    ]
