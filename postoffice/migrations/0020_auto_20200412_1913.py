# Generated by Django 3.0.5 on 2020-04-12 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postoffice', '0019_auto_20200411_0237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packages',
            name='signature',
        ),
        migrations.AddField(
            model_name='packages',
            name='start_location',
            field=models.ForeignKey(default=8888, on_delete=django.db.models.deletion.CASCADE, to='postoffice.branches'),
            preserve_default=False,
        ),
    ]