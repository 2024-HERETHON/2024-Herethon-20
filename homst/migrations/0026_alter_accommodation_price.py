# Generated by Django 4.2.11 on 2024-07-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homst', '0025_sortoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
