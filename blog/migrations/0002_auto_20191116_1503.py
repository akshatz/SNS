# Generated by Django 2.2.6 on 2019-11-16 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together={('user_id', 'friend_id')},
        ),
    ]
