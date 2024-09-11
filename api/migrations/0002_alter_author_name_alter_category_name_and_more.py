# Generated by Django 4.2.16 on 2024-09-10 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('TECH', 'TECH'), ('HEALTH', 'HEALTH'), ('FINANCE', 'FINANCE'), ('LEADERSHIP', 'LEADERSHIP')], max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='concept',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
