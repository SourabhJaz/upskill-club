# Generated by Django 4.2.16 on 2024-09-12 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_category_thumbnail_alter_concept_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
