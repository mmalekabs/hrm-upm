# Generated by Django 2.2.5 on 2022-03-12 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20220312_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_DOB',
            field=models.DateField(),
        ),
    ]