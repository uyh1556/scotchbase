# Generated by Django 4.2.13 on 2024-06-26 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whisky', '0003_whisky_abv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whisky',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
