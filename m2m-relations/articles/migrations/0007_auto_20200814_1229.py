# Generated by Django 3.0.8 on 2020-08-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20200814_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='main',
        ),
        migrations.AddField(
            model_name='section',
            name='main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
    ]
