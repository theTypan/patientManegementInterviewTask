# Generated by Django 2.0.6 on 2018-06-24 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_nextofkin_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='nextofkin',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]