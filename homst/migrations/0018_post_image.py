# Generated by Django 4.2.11 on 2024-07-03 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homst', '0017_remove_post_updated_at_alter_accommodation_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
