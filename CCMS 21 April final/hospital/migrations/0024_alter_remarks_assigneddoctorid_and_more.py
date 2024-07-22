# Generated by Django 4.2.6 on 2024-04-13 13:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hospital", "0023_remarks_remove_patient_remarks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="remarks",
            name="assignedDoctorId",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="remarks",
            name="patientId",
            field=models.IntegerField(null=True),
        ),
    ]
