# Generated by Django 4.2.7 on 2023-11-13 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviewApp', '0012_instructor_reviewer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='reviewer',
        ),
        migrations.AddField(
            model_name='instructor',
            name='student_reviewer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='given_instructor_reviews', to='reviewApp.student'),
        ),
    ]
