# Generated by Django 4.0.1 on 2022-01-08 15:23

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0006_alter_statusmodels_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusmodels',
            name='HP',
            field=models.PositiveBigIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='statusmodels',
            name='MP',
            field=models.PositiveBigIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='statusmodels',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0208b218-e816-47e7-a7e6-c2f2eb166f10'), editable=False, primary_key=True, serialize=False),
        ),
    ]
