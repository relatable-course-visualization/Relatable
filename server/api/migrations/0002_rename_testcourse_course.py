# Generated by Django 4.1.2 on 2022-11-05 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestCourse',
            new_name='Course',
        ),
    ]
