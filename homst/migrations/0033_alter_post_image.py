# Generated by Django 4.2.11 on 2024-07-04 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homst', '0032_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post/'),
        ),
    ]
