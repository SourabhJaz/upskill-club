# Generated by Django 4.2.16 on 2024-09-13 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_course_created_at_session_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='created_at',
            field=models.DateField(null=True),
        ),
    ]