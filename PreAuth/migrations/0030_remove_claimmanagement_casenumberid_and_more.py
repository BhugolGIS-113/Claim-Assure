# Generated by Django 4.1.5 on 2023-03-01 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PreAuth', '0029_rename_folder_path_shapefiles_folder_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='claimmanagement',
            name='CaseNumberID',
        ),
        migrations.RemoveField(
            model_name='claimmanagement',
            name='user',
        ),
        migrations.DeleteModel(
            name='DumpExcel',
        ),
        migrations.DeleteModel(
            name='ClaimManagement',
        ),
    ]
