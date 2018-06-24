# Generated by Django 2.0.6 on 2018-06-24 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_nextofkin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.County'),
        ),
        migrations.AlterField(
            model_name='user',
            name='subcounty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.Subcounty'),
        ),
        migrations.AlterField(
            model_name='user',
            name='village',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.Village'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.Ward'),
        ),
    ]