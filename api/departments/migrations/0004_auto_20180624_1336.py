# Generated by Django 2.0.6 on 2018-06-24 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0003_auto_20180624_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentpatient',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]