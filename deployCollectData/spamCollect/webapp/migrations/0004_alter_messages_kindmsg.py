# Generated by Django 4.2 on 2023-05-01 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_messages_kindmsg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='kindmsg',
            field=models.BooleanField(),
        ),
    ]