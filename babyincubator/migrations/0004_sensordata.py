# Generated by Django 4.1.3 on 2024-05-27 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babyincubator', '0003_babys_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='sensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('air_quality', models.CharField(max_length=50)),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('rain_detected', models.BooleanField()),
                ('sound_level', models.FloatField()),
            ],
        ),
    ]