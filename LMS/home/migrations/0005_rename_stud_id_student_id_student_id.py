# Generated by Django 5.1.3 on 2024-11-08 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_depart_department_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_id',
            old_name='stud_id',
            new_name='student_id',
        ),
    ]