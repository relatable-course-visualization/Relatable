# Generated by Django 4.0.4 on 2023-06-04 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_coursetable2023_not_in_catalogue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursetable2023',
            name='not_in_catalogue',
            field=models.BooleanField(default=False),
        ),
    ]
