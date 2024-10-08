# Generated by Django 4.2.16 on 2024-09-23 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_author_linkedinurl_remove_author_thumbnail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='linkedin_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='concept',
            name='image_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='image_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='image_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
