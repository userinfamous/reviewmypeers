# Generated by Django 4.2.7 on 2023-11-11 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewApp', '0008_instructor_class_code_instructor_class_taught_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='student_id',
        ),
    ]
