# Generated by Django 3.0.8 on 2020-08-13 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200813_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='articles',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(through='articles.Section', to='articles.Tag'),
        ),
    ]
