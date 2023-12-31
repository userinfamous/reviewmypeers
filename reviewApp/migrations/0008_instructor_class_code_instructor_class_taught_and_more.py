# Generated by Django 4.2.7 on 2023-11-11 15:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewApp', '0007_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='class_code',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='instructor',
            name='class_taught',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='instructor',
            name='text',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='review',
            name='agreeable',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='charisma',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='class_code',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='review',
            name='leadership_skills',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='pragmatic',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='reliability',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='review',
            name='trustworthiness',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
