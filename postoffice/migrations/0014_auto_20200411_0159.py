# Generated by Django 3.0.3 on 2020-04-11 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postoffice', '0013_auto_20200410_0425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package_history',
            old_name='current_location',
            new_name='current_location_id',
        ),
    ]
