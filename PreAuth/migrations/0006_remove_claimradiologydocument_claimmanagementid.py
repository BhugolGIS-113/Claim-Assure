# Generated by Django 4.1.5 on 2023-02-22 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PreAuth', '0005_remove_claimmanagement_radiology_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='claimradiologydocument',
            name='ClaimManagementID',
        ),
    ]
