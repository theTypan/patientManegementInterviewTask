# Generated by Django 2.0.6 on 2018-06-24 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0007_auto_20180624_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
