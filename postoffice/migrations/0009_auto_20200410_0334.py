# Generated by Django 3.0.3 on 2020-04-10 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postoffice', '0008_package_history'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package_history',
            old_name='package',
            new_name='package_ID',
        ),
    ]
