# Generated by Django 4.2.6 on 2024-04-12 14:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("hospital", "0019_patient_remarks"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="patient",
            name="remarks",
        ),
    ]
