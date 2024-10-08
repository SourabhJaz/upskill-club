# Generated by Django 4.2.16 on 2024-09-10 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('linkedInUrl', models.URLField()),
                ('outline', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('TECH', 'TECH'), ('HEALTH', 'HEALTH'), ('FINANCE', 'FINANCE'), ('LEADERSHIP', 'LEADERSHIP')], max_length=15)),
                ('outline', models.CharField(max_length=200)),
                ('thumbnail', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('outline', models.CharField(max_length=200)),
                ('short_description', models.CharField(max_length=500)),
                ('thumbnail', models.FileField(upload_to='')),
                ('image', models.FileField(null=True, upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('outline', models.CharField(max_length=200)),
                ('thumbnail', models.FileField(upload_to='')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course')),
            ],
        ),
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.FileField(null=True, upload_to='')),
                ('description', models.CharField(max_length=1500)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.session')),
            ],
        ),
    ]
