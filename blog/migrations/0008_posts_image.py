# Generated by Django 2.2.7 on 2019-11-05 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191105_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to='posts'),
        ),
    ]
