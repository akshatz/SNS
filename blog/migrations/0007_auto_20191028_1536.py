# Generated by Django 2.2.6 on 2019-10-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191028_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts/'),
        ),
    ]
