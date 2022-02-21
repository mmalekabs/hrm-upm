# Generated by Django 2.2.5 on 2022-02-21 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addresses',
            fields=[
                ('address_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('address_building_number', models.IntegerField()),
                ('address_street_name', models.CharField(max_length=24)),
                ('address_district_name', models.CharField(max_length=24)),
                ('address_city_name', models.CharField(max_length=24)),
                ('address_zip_code', models.IntegerField()),
                ('address_additional_number', models.IntegerField()),
                ('address_unit_number', models.IntegerField()),
                ('address_created_at', models.DateTimeField()),
                ('address_updated_at', models.DateTimeField()),
                ('address_deleted_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='attachment_types',
            fields=[
                ('attachment_type_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('attachment_type_name', models.CharField(max_length=24)),
                ('attachment_type_status', models.IntegerField()),
                ('attachment_type_created_at', models.DateTimeField()),
                ('attachment_type_updated_at', models.DateTimeField()),
                ('attachment_type_deleted_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='attachments',
            fields=[
                ('attachment_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('attachment_name', models.CharField(max_length=50)),
                ('attachment_type', models.CharField(max_length=24)),
                ('attachment_path', models.TextField()),
                ('attachment_created_at', models.DateTimeField()),
                ('attachment_updated_at', models.DateTimeField()),
                ('attachment_deleted_at', models.DateTimeField()),
                ('attachment_attachment_type_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.attachment_types')),
            ],
        ),
        migrations.CreateModel(
            name='countries',
            fields=[
                ('country_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('country_ISO3', models.IntegerField()),
                ('country_ISO2', models.IntegerField()),
                ('country_arabic_name', models.CharField(max_length=264)),
                ('country_english_name', models.CharField(max_length=264)),
                ('country_nationality_arabic', models.CharField(max_length=264)),
                ('country_nationality_english', models.CharField(max_length=264)),
                ('country_flag', models.CharField(max_length=6)),
                ('country_currency_name', models.CharField(max_length=50)),
                ('country_code', models.CharField(max_length=5)),
                ('country_currency_symbol', models.CharField(max_length=5)),
                ('country_domain', models.CharField(max_length=10)),
                ('country_dial_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='permissions',
            fields=[
                ('permission_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('permission_name', models.CharField(max_length=50)),
                ('permission_created_at', models.DateTimeField()),
                ('permission_updated_at', models.DateTimeField()),
                ('permission_deleted_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='roles',
            fields=[
                ('role_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=50)),
                ('roles_created_at', models.DateTimeField()),
                ('role_updated_at', models.DateTimeField()),
                ('role_deleted_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='user_types',
            fields=[
                ('user_type_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('user_type_created_at', models.DateTimeField()),
                ('user_type_updated_at', models.DateTimeField()),
                ('user_type_deleted_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('user_first_name', models.CharField(max_length=24)),
                ('user_middle_name', models.CharField(max_length=24)),
                ('user_last_name', models.CharField(max_length=24)),
                ('user_email', models.CharField(max_length=50, unique=True)),
                ('user_mobile', models.IntegerField(unique=True)),
                ('user_password_hash', models.TextField()),
                ('user_activation_hash', models.TextField()),
                ('user_is_active', models.BooleanField()),
                ('user_status', models.BooleanField()),
                ('user_education_degree', models.CharField(max_length=24)),
                ('user_DOB', models.DateField()),
                ('user_nationality_ID', models.IntegerField()),
                ('user_created_at', models.DateTimeField()),
                ('user_updated_at', models.DateTimeField()),
                ('user_deleted_at', models.DateTimeField()),
                ('user_address_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.addresses')),
                ('user_attachment_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.attachments')),
                ('user_employee_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='job_management.departments')),
                ('user_job_title_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='job_management.job_titles')),
                ('user_type_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.user_types')),
            ],
        ),
        migrations.AddField(
            model_name='user_types',
            name='user_type_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.users'),
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('skill_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('skill_name', models.CharField(max_length=50)),
                ('skill_rating', models.IntegerField()),
                ('skill_created_at', models.DateTimeField()),
                ('skill_updated_at', models.DateTimeField()),
                ('skill_deleted_at', models.DateTimeField()),
                ('skill_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.users')),
            ],
        ),
        migrations.CreateModel(
            name='roles_and_permissions',
            fields=[
                ('role_and_permission_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('role_and_permission_name', models.CharField(max_length=50)),
                ('role_and_permission_level', models.IntegerField()),
                ('role_and_permission_created_at', models.DateTimeField()),
                ('role_and_permission_updated_at', models.DateTimeField()),
                ('role_and_permission_name_deleted_at', models.DateTimeField()),
                ('role_and_permission_permissions_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.permissions')),
                ('role_and_permission_role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.roles')),
            ],
        ),
        migrations.CreateModel(
            name='courses',
            fields=[
                ('course_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('course_title', models.CharField(max_length=264)),
                ('course_DOC', models.DateField()),
                ('course_length', models.IntegerField()),
                ('course_provider', models.CharField(max_length=264)),
                ('course_created_at', models.DateTimeField()),
                ('course_updated_at', models.DateTimeField()),
                ('course_deleted_at', models.DateTimeField()),
                ('course_attachments_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.attachments')),
                ('course_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.users')),
            ],
        ),
        migrations.CreateModel(
            name='attachments_users',
            fields=[
                ('attachment_user_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('attachment_user_created_at', models.DateTimeField()),
                ('attachment_user_updated_at', models.DateTimeField()),
                ('attachment_user_deleted_at', models.DateTimeField()),
                ('attachment_user_attachment_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.attachments')),
                ('attachment_user_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.users')),
            ],
        ),
        migrations.AddField(
            model_name='addresses',
            name='address_country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.countries'),
        ),
        migrations.AddField(
            model_name='addresses',
            name='address_created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.users'),
        ),
    ]
