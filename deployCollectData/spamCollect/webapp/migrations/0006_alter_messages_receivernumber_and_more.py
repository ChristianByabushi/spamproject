# Generated by Django 4.2 on 2023-05-01 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_messages_age_alter_messages_sendernumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='receiverNumber',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='senderNumber',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]