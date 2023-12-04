# Generated by Django 4.2.7 on 2023-11-13 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviewApp', '0016_alter_instructor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='instructorreview',
            name='student_reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='given_instructor_reviews', to='reviewApp.student'),
        ),
    ]