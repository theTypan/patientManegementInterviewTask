# Generated by Django 2.0.6 on 2018-06-24 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20180624_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_patient',
            field=models.BooleanField(default=False),
        ),
    ]
