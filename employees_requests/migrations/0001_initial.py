# Generated by Django 2.2.5 on 2022-02-21 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='complains_and_suggestions',
            fields=[
                ('complains_and_suggestions_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('complains_or_suggestions', models.BooleanField()),
                ('complains_and_suggestions_created_at', models.DateTimeField()),
                ('complains_and_suggestions_updated_at', models.DateTimeField()),
                ('complains_and_suggestions_deleted_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='loans',
            fields=[
                ('loan_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('loan_type', models.CharField(max_length=24)),
                ('loan_amount', models.IntegerField()),
                ('loan_started_date', models.DateField()),
                ('loan_period', models.IntegerField()),
                ('loan_number_of_complete_payment', models.IntegerField()),
                ('loan_status', models.BooleanField()),
                ('loan_admin_approval', models.BooleanField()),
                ('loan_created_at', models.DateTimeField()),
                ('loan_updated_at', models.DateTimeField()),
                ('loan_deleted_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='overtime',
            fields=[
                ('overtime_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('overtime_status', models.BooleanField()),
                ('overtime_hours', models.IntegerField()),
                ('overtime_amount', models.IntegerField()),
                ('overtime_created_at', models.DateTimeField()),
                ('overtime_updated_at', models.DateTimeField()),
                ('overtime_deleted_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='overtime_types',
            fields=[
                ('overtime_type_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('overtime_type_name', models.CharField(max_length=50)),
                ('overtime_type_created_at', models.DateTimeField()),
                ('overtime_type_updated_at', models.DateTimeField()),
                ('overtime_type_deleted_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='vacations',
            fields=[
                ('vacation_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('vacation_leaving_date', models.DateField()),
                ('vacation_coming_date', models.DateField()),
                ('vacation_is_paid', models.BooleanField()),
                ('vacation_created_at', models.DateTimeField()),
                ('vacation_updated_at', models.DateTimeField()),
                ('vacation_deleted_at', models.DateTimeField()),
            ],
        ),
    ]
