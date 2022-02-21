# Generated by Django 2.2.5 on 2022-02-21 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='evaluations',
            fields=[
                ('evaluation_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('evaluation_interaction_rate', models.IntegerField()),
                ('evaluation_time_rate', models.IntegerField()),
                ('evaluation_quality_rate', models.IntegerField()),
                ('evaluation_created_at', models.DateTimeField()),
                ('evaluation_updated_at', models.DateTimeField()),
                ('evaluation_deleted_at', models.DateTimeField()),
                ('evaluation_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('attendance_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('attendance_clock_in', models.DateTimeField()),
                ('attendance_clock_out', models.DateTimeField()),
                ('attendance_total_hours', models.IntegerField()),
                ('attendance_half_day', models.BooleanField()),
                ('attendance_working_from', models.CharField(max_length=24)),
                ('attendance_created_at', models.DateTimeField()),
                ('attendance_updated_at', models.DateTimeField()),
                ('attendance_deleted_at', models.DateTimeField()),
                ('attendance_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.users')),
            ],
        ),
    ]
