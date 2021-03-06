# Generated by Django 3.0.3 on 2020-04-11 07:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('postoffice', '0014_auto_20200411_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='location_mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('current_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postoffice.branches')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='postoffice.Packages')),
            ],
        ),
    ]
