# Generated by Django 4.1.5 on 2023-02-23 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PreAuth', '0008_delete_claimradiologydocument_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DumpExcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CaseNo', models.CharField(blank=True, max_length=255, null=True)),
                ('ClaimNo', models.CharField(blank=True, max_length=255, null=True)),
                ('RegistrationNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('NHPMId', models.CharField(blank=True, max_length=255, null=True)),
                ('FamilyId', models.CharField(blank=True, max_length=255, null=True)),
                ('PatientDistrict', models.CharField(blank=True, max_length=255, null=True)),
                ('Gender', models.CharField(blank=True, max_length=255, null=True)),
                ('Age', models.IntegerField()),
                ('CategoryDetails', models.CharField(blank=True, max_length=255, null=True)),
                ('ProcedureDetails', models.CharField(blank=True, max_length=255, null=True)),
                ('CaseType', models.CharField(blank=True, max_length=255, null=True)),
                ('CaseStatus', models.CharField(blank=True, max_length=255, null=True)),
                ('HospitalName', models.CharField(blank=True, max_length=255, null=True)),
                ('HospitalCode', models.CharField(blank=True, max_length=255, null=True)),
                ('HospitalDistrict', models.CharField(blank=True, max_length=255, null=True)),
                ('IPRegistrationDate', models.DateTimeField(blank=True, null=True)),
                ('AdmissionDate', models.DateTimeField(blank=True, null=True)),
                ('PreauthDate', models.DateTimeField(blank=True, null=True)),
                ('PreauthAmount', models.IntegerField()),
                ('PreauthApproveDate', models.DateTimeField(blank=True, null=True)),
                ('PreauthApprovedAmount', models.IntegerField()),
                ('PreauthRejectedDate', models.DateTimeField(blank=True, null=True)),
                ('SurgeryDate', models.DateTimeField(blank=True, null=True)),
                ('DeathDate', models.DateTimeField(blank=True, null=True)),
                ('DischargeDate', models.DateTimeField(blank=True, null=True)),
                ('ClaimSubmittedDate', models.DateTimeField(blank=True, null=True)),
                ('ActualClaimSubmittedDate', models.DateTimeField(blank=True, null=True)),
                ('ClaimInitaiatedAmount', models.IntegerField()),
                ('CPDApprovedAmount', models.IntegerField()),
                ('ClaimApprovedAmount', models.CharField(blank=True, max_length=255, null=True)),
                ('AssignedFlag', models.CharField(blank=True, max_length=255, null=True)),
                ('AssignedUser', models.CharField(blank=True, max_length=255, null=True)),
                ('AssignedGroup', models.CharField(blank=True, max_length=255, null=True)),
                ('IPNumber', models.IntegerField()),
                ('ActualRegistrationDate', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
