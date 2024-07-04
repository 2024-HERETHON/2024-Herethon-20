# Generated by Django 4.2.13 on 2024-07-02 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homst', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='safetyfilter',
            name='category',
            field=models.CharField(choices=[('female', '여성 전용 숙소'), ('mole_care', '몰카 안심 숙소'), ('restroom_separated', '화장실 남녀 분리'), ('cctv', 'CCTV 설치 유무')], default='female', max_length=50),
        ),
    ]
