# Generated by Django 4.1.1 on 2022-09-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='datecomplete',
        ),
        migrations.AddField(
            model_name='tasks',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]