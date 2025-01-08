# Generated by Django 5.1.1 on 2024-10-19 09:31

import webapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_students_photo1_alter_students_photo2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='photo1',
            field=models.ImageField(max_length=300, upload_to=webapp.models.Rename.save),
        ),
        migrations.AlterField(
            model_name='students',
            name='photo2',
            field=models.ImageField(blank=True, max_length=300, upload_to=webapp.models.Rename.save),
        ),
        migrations.AlterField(
            model_name='students',
            name='photo3',
            field=models.ImageField(blank=True, max_length=300, upload_to=webapp.models.Rename.save),
        ),
    ]
