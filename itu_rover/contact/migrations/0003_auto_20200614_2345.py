# Generated by Django 2.0.1 on 2020-06-14 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200614_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='joinform',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='supportform',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
