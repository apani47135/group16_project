# Generated by Django 3.0.5 on 2020-04-03 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postoffice', '0006_auto_20200403_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='sent_by',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='postoffice.Sender'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='packages',
            name='sent_to',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='postoffice.reciever'),
            preserve_default=False,
        ),
    ]
