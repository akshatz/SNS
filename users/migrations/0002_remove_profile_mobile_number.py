# Generated by Django 2.2 on 2019-10-29 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='mobile_number',
        ),
    ]
