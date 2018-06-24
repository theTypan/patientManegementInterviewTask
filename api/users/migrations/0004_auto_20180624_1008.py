# Generated by Django 2.0.6 on 2018-06-24 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20180624_1008'),
        ('users', '0003_auto_20180624_0854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='location',
        ),
        migrations.AddField(
            model_name='user',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.County'),
        ),
        migrations.AddField(
            model_name='user',
            name='subcounty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.Subcounty'),
        ),
        migrations.AddField(
            model_name='user',
            name='village',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.Village'),
        ),
        migrations.AddField(
            model_name='user',
            name='ward',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.Ward'),
        ),
    ]