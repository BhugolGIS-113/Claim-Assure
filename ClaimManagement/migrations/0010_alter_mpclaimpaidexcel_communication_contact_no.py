# Generated by Django 4.1.5 on 2023-03-09 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClaimManagement', '0009_alter_mpclaimpaidexcel_cpd_processing_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpclaimpaidexcel',
            name='Communication_Contact_No',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]