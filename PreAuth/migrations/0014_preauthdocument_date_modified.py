# Generated by Django 4.1.5 on 2023-02-25 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PreAuth', '0013_alter_dumpexcel_actualclaimsubmitteddate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='preauthdocument',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
