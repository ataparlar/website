# Generated by Django 2.0.1 on 2020-07-24 23:37

from django.db import migrations, models
import main.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainPageEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('is_old', models.BooleanField(default=False, help_text='is this entry still newsworthy??')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('title', models.CharField(max_length=20)),
                ('place', models.SmallIntegerField(default=0)),
                ('bg_image', models.ImageField(upload_to=main.utils.slider_image_upload_to)),
                ('rover_image', models.ImageField(upload_to=main.utils.slider_image_upload_to)),
                ('grade', models.TextField(blank=True, null=True)),
                ('show_title', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
