# Generated by Django 4.2.11 on 2024-07-06 02:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homst', '0038_post_accommodation_name_post_travel_destination'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateField(auto_now_add=True)),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homst.accommodation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
