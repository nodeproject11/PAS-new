# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-24 06:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('day', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=200)),
                ('contactperson', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptt_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Dual_Datas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internship', models.CharField(max_length=200)),
                ('place_of_internship', models.CharField(max_length=200)),
                ('ppo', models.CharField(max_length=200)),
                ('spo_internship', models.CharField(max_length=200)),
                ('ug_cpi', models.DecimalField(decimal_places=3, max_digits=5)),
                ('pg_cpi', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Job_Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Job_Openings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('internship', models.BooleanField()),
                ('package_btech', models.CharField(max_length=200)),
                ('package_mtech', models.CharField(max_length=200)),
                ('package_dual', models.CharField(max_length=200)),
                ('package_msci', models.CharField(max_length=200)),
                ('package_msc2', models.CharField(max_length=200)),
                ('package_mba', models.CharField(max_length=200)),
                ('package_mdes', models.CharField(max_length=200)),
                ('package_phd', models.CharField(max_length=200)),
                ('package_details', models.CharField(max_length=200)),
                ('bond', models.BooleanField()),
                ('bond_details', models.CharField(max_length=200)),
                ('medical_requirments', models.CharField(max_length=200)),
                ('resume_shortlist', models.BooleanField()),
                ('resume_criteria', models.CharField(max_length=200)),
                ('aptitude', models.BooleanField()),
                ('group_discussion', models.BooleanField()),
                ('tech_test', models.BooleanField()),
                ('tech_interview', models.BooleanField()),
                ('hr_interview', models.BooleanField()),
                ('number_of_rounds', models.IntegerField(default=0)),
                ('contact_details1', models.CharField(max_length=1024)),
                ('contact_details2', models.CharField(max_length=1024)),
                ('contact_details3', models.CharField(max_length=1024)),
                ('application_deadline', models.DateField()),
                ('eligiblity', models.CharField(max_length=1024)),
                ('name', models.CharField(max_length=200)),
                ('published', models.BooleanField()),
                ('deadline', models.DateField()),
                ('ctc_btech', models.CharField(max_length=200)),
                ('ctc_mtech', models.CharField(max_length=200)),
                ('ctc_dual', models.CharField(max_length=200)),
                ('ctc_msci', models.CharField(max_length=200)),
                ('ctc_msc2', models.CharField(max_length=200)),
                ('ctc_mba', models.CharField(max_length=200)),
                ('ctc_mdes', models.CharField(max_length=200)),
                ('ctc_phd', models.CharField(max_length=200)),
                ('aptitude_duration', models.CharField(max_length=200)),
                ('tech_test_duration', models.CharField(max_length=200)),
                ('gd_duration', models.CharField(max_length=200)),
                ('gd_strength', models.CharField(max_length=200)),
                ('tech_interview_duration', models.CharField(max_length=200)),
                ('hr_interview_duration', models.CharField(max_length=200)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addy.Companies')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('time_date', models.DateTimeField(verbose_name='Date Published')),
                ('job_opening', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addy.Job_Openings')),
            ],
        ),
        migrations.CreateModel(
            name='Pg_Datas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ug_college', models.CharField(max_length=200)),
                ('funding_institute', models.CharField(max_length=200)),
                ('sponsored', models.CharField(max_length=200)),
                ('work_experience', models.CharField(max_length=200)),
                ('ug_marks', models.DecimalField(decimal_places=3, max_digits=5)),
                ('ug_marks_scale', models.IntegerField()),
                ('name_of_degree', models.CharField(max_length=200)),
                ('year_of_ug', models.IntegerField()),
                ('specialisation', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Phd_Datas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pg_marks', models.DecimalField(decimal_places=3, max_digits=5)),
                ('pg_marks_scale', models.IntegerField()),
                ('name_of_pg_degree', models.CharField(max_length=200)),
                ('sponsored', models.CharField(max_length=200)),
                ('funding_institute', models.CharField(max_length=200)),
                ('phd_thesis', models.CharField(max_length=200)),
                ('work_experience', models.CharField(max_length=200)),
                ('pg_university', models.CharField(max_length=200)),
                ('pg_thesis', models.CharField(max_length=200)),
                ('pg_super1_name', models.EmailField(max_length=200)),
                ('pg_super2_name', models.EmailField(max_length=200)),
                ('pg_specialisation', models.CharField(max_length=200)),
                ('year_of_pg', models.IntegerField()),
                ('ug_marks', models.DecimalField(decimal_places=3, max_digits=5)),
                ('ug_marks_scale', models.IntegerField()),
                ('ug_college', models.CharField(max_length=200)),
                ('name_of_ug_degree', models.CharField(max_length=200)),
                ('ug_specialisation', models.CharField(max_length=200)),
                ('year_of_ug', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.IntegerField()),
                ('spo_registration_number', models.IntegerField(default=0)),
                ('full_name', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('dob', models.DateField()),
                ('category', models.CharField(choices=[('GN', 'General'), ('SC', 'SC'), ('ST', 'ST'), ('OTHERS', 'Other')], default='GN', max_length=50)),
                ('local_address', models.CharField(max_length=1000)),
                ('permanent_address', models.CharField(max_length=1000)),
                ('mobile_number', models.IntegerField(default=0)),
                ('friend_mobile_number', models.IntegerField(default=0)),
                ('phone_number', models.IntegerField(default=0)),
                ('emergency_number1', models.IntegerField(default=0)),
                ('emergency_number2', models.IntegerField(default=0)),
                ('emergency_name1', models.CharField(max_length=200)),
                ('emergency_name2', models.CharField(max_length=200)),
                ('email_iitk', models.EmailField(max_length=200)),
                ('entrance_rank', models.IntegerField(default=0)),
                ('cpi', models.DecimalField(decimal_places=3, max_digits=5)),
                ('expected_graduation_date', models.DateField()),
                ('marks_10', models.FloatField()),
                ('year_10', models.IntegerField()),
                ('board_10', models.CharField(max_length=200)),
                ('marks_12', models.FloatField()),
                ('year_12', models.IntegerField()),
                ('board_12', models.CharField(max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addy.Department')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addy.Program')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Temp_Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('student_roll', models.IntegerField()),
                ('student_username', models.CharField(max_length=200)),
                ('student_isAccepted', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ug_Datas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internship', models.CharField(max_length=200)),
                ('place_of_internship', models.CharField(max_length=200)),
                ('ppo', models.CharField(max_length=200)),
                ('spo_internship', models.CharField(max_length=200)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='addy.Student')),
            ],
        ),
        migrations.AddField(
            model_name='phd_datas',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='addy.Student'),
        ),
        migrations.AddField(
            model_name='pg_datas',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='addy.Student'),
        ),
        migrations.AddField(
            model_name='job_application',
            name='job_opening',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addy.Job_Openings'),
        ),
        migrations.AddField(
            model_name='job_application',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addy.Student'),
        ),
        migrations.AddField(
            model_name='dual_datas',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='addy.Student'),
        ),
    ]
