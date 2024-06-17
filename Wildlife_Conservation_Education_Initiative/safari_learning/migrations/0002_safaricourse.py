# Generated by Django 4.2.7 on 2024-06-14 09:42

from django.db import migrations, models
import safari_learning.models


class Migration(migrations.Migration):

    dependencies = [
        ('safari_learning', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SafariCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_link', models.URLField(max_length=600)),
                ('file_name', models.FilePathField(match='\\.(jpg|jpeg|png|gif|bmp)$', path=safari_learning.models.images_path)),
                ('profession_json', models.JSONField()),
            ],
        ),
    ]