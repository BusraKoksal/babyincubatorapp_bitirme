# Generated by Django 4.1.3 on 2024-05-23 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Babys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bebek_adi', models.CharField(max_length=100)),
                ('aciklama', models.TextField()),
                ('resim', models.CharField(max_length=100)),
                ('anasayfa', models.BooleanField(default=False)),
            ],
        ),
    ]
