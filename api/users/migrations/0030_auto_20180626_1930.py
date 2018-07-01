# Generated by Django 2.0.6 on 2018-06-26 19:30

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_user_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='primary_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, null=True, unique=True),
        ),
    ]