# Generated by Django 5.1.3 on 2024-11-27 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctors", "0002_doctor_is_on_vacation"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="graduation_date",
            field=models.DateField(default=None, null=True),
            preserve_default=False,
        ),
    ]
