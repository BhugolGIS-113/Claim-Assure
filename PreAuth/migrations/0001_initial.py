# Generated by Django 4.1.5 on 2023-02-16 06:10

import PreAuth.models
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
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NHPMID', models.CharField(max_length=255, unique=True)),
                ('nameOfPatient', models.CharField(max_length=255)),
                ('adharPhotograph', models.ImageField(blank=True, null=True, upload_to='AdharCard_PhotoGraphs')),
                ('adharNumber', models.PositiveBigIntegerField(unique=True, validators=[PreAuth.models.validate_length])),
                ('DOB', models.DateField()),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('mobileNumber', models.PositiveBigIntegerField(blank=True, null=True, validators=[PreAuth.models.validate_number])),
                ('alternativeNumber', models.PositiveBigIntegerField(blank=True, null=True, validators=[PreAuth.models.validate_number])),
                ('addressLine1', models.CharField(blank=True, max_length=255, null=True)),
                ('addressLine2', models.CharField(blank=True, max_length=255, null=True)),
                ('district', models.CharField(blank=True, max_length=50, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('RationCardNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('RationCardPhotograph', models.ImageField(blank=True, null=True, upload_to='RationCard_Photographs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PreAuthDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PreAuthID', models.CharField(max_length=255, unique=True)),
                ('dateOfAdmission', models.DateTimeField()),
                ('dateOfPreAuth', models.DateTimeField()),
                ('hospitalName', models.CharField(max_length=255)),
                ('hospitalCode', models.CharField(max_length=255)),
                ('justification', models.FileField(blank=True, null=True, upload_to='PreAuthDocuments/justification')),
                ('on_BedPhotograph', models.FileField(blank=True, null=True, upload_to='PreAuthDocuments/on_bedPhotograph')),
                ('admitCaseSheet', models.FileField(blank=True, null=True, upload_to='PreAuthDocuments/admitCaseSheet')),
                ('labReport', models.FileField(blank=True, null=True, upload_to='PreAuthDocuments/labReport')),
                ('radiologyReport', models.FileField(blank=True, null=True, upload_to='PreAuthDocuments/radiologyReport')),
                ('PersonalInfoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PreAuth_personal', to='PreAuth.personalinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Preauth_document', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PreAuthLinkCaseNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CaseNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('PreAuthID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='PreAuth_PreAuthID', to='PreAuth.preauthdocument')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PreAuthLinkCaseNumber_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
