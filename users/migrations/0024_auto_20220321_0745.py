# Generated by Django 2.2.5 on 2022-03-21 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20220320_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='users',
            name='user_deleted_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='user_updated_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
