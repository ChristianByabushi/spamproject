# Generated by Django 4.2 on 2023-05-01 21:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_messages_kindmsg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='age',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(120)]),
        ),
        migrations.AlterField(
            model_name='messages',
            name='senderNumber',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
