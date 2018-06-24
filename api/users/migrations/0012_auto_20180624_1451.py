# Generated by Django 2.0.6 on 2018-06-24 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20180624_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nextofkin',
            name='next_of_kin',
            field=models.ManyToManyField(blank=True, null=True, related_name='next_of_kins', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='nextofkin',
            name='user',
        ),
        migrations.AddField(
            model_name='nextofkin',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
