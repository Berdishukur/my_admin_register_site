# Generated by Django 4.0.6 on 2023-07-18 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_alter_students_first_name_alter_students_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
