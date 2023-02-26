# Generated by Django 4.1.5 on 2023-02-26 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PreAuth', '0017_alter_dumpexcel_categorydetails_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dumpexcel',
            name='CaseStatus',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dumpexcel',
            name='CaseType',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dumpexcel',
            name='ClaimInitaiatedAmount',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dumpexcel',
            name='HospitalCode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dumpexcel',
            name='HospitalDistrict',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dumpexcel',
            name='HospitalName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dumpexcel',
            name='PreauthAmount',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
