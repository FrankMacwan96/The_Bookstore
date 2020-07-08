# Generated by Django 2.2.5 on 2019-12-04 22:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyAppIADS', '0006_auto_20191113_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)]),
        ),
    ]