# Generated by Django 2.2.5 on 2022-03-03 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220303_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_first_name',
            field=models.CharField(default='firstname', max_length=24),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='user_last_name',
            field=models.CharField(default='lastname', max_length=24),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='user_middle_name',
            field=models.CharField(default='middlename', max_length=24),
            preserve_default=False,
        ),
    ]