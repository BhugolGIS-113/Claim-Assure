# Generated by Django 4.1.5 on 2023-03-09 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClaimManagement', '0010_alter_mpclaimpaidexcel_communication_contact_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpclaimpaidexcel',
            name='CPD_Processing_Time',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
