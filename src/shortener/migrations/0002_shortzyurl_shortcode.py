# Generated by Django 5.2 on 2025-05-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortzyurl',
            name='shortcode',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
