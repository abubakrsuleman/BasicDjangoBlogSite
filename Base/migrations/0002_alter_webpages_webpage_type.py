# Generated by Django 4.2.2 on 2023-08-22 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpages',
            name='webpage_type',
            field=models.CharField(choices=[('ABOUT', 'About')], max_length=8),
        ),
    ]
