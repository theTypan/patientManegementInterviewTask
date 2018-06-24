# Generated by Django 2.0.6 on 2018-06-24 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0006_auto_20180624_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='departments.Department'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_patients', to=settings.AUTH_USER_MODEL),
        ),
    ]
