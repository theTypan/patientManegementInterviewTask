# Generated by Django 2.0.6 on 2018-07-02 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('enrollment_date', models.DateTimeField()),
                ('discharged', models.BooleanField(default=False)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='departments.Department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
