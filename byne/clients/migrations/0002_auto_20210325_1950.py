# Generated by Django 3.1.7 on 2021-03-25 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='log',
            field=models.JSONField(default={}),
        ),
        migrations.AddField(
            model_name='profile',
            name='loglist',
            field=models.JSONField(default=[]),
        ),
    ]
