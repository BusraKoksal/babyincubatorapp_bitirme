# Generated by Django 4.1.3 on 2024-05-26 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babyincubator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ebeveyn_bilgi', models.CharField(max_length=250)),
                ('ebeveyn_iletisim', models.EmailField(max_length=254)),
            ],
        ),
    ]
