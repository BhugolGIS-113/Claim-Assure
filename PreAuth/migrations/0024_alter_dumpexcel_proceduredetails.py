# Generated by Django 4.1.5 on 2023-02-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PreAuth', '0023_alter_dumpexcel_proceduredetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dumpexcel',
            name='ProcedureDetails',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]