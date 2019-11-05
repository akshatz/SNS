# Generated by Django 2.2.7 on 2019-11-05 07:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('blog', '0006_remove_user_friend_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friend_id',
            field=models.ManyToManyField(related_name='_user_friend_id_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='PostDetailView',
        ),
    ]
