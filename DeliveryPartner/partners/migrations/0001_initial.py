# Generated by Django 4.1.1 on 2023-06-28 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('tradingName', models.CharField(max_length=255)),
                ('ownerName', models.CharField(max_length=255)),
                ('document', models.FileField(blank=True, unique=True, upload_to='partners/documents')),
                ('coverageArea', models.JSONField()),
                ('address', models.JSONField()),
            ],
        ),
    ]
