# Generated by Django 5.1.5 on 2025-03-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intensity', models.FloatField()),
                ('likelihood', models.FloatField()),
                ('relevance', models.FloatField()),
                ('year', models.IntegerField()),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('topics', models.CharField(blank=True, max_length=255, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
