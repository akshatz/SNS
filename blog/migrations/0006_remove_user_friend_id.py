# Generated by Django 2.2.7 on 2019-11-04 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_posts_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='friend_id',
        ),
    ]
