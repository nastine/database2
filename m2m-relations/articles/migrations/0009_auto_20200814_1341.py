# Generated by Django 3.0.8 on 2020-08-14 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20200814_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='scope',
            new_name='scopes',
        ),
        migrations.AlterField(
            model_name='scope',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
