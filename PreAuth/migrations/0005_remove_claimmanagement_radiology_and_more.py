# Generated by Django 4.1.5 on 2023-02-22 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PreAuth', '0004_claimmanagement_casenumberid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='claimmanagement',
            name='Radiology',
        ),
        migrations.CreateModel(
            name='ClaimRadiologyDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Radiology', models.FileField(blank=True, null=True, upload_to='ClaimDocuments/Reports')),
                ('ClaimManagementID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ClaimRadiologyDocument_id', to='PreAuth.claimmanagement')),
            ],
        ),
    ]