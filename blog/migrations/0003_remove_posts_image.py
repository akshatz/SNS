# Generated by Django 2.2.7 on 2019-11-04 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postdetailview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='image',
        ),
    ]
