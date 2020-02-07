# Generated by Django 2.0.1 on 2020-02-07 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0019_auto_20190325_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='did_work',
            field=models.BooleanField(default=False, verbose_name="if True: This person will be shown on 'graduated' pagewith the infos of 'working' and 'eng_working'"),
        ),
        migrations.AddField(
            model_name='member',
            name='eng_description',
            field=models.CharField(blank=True, max_length=75, verbose_name='english description (e.g. department)'),
        ),
        migrations.AddField(
            model_name='member',
            name='eng_working',
            field=models.TextField(blank=True, null=True, verbose_name='english working experiences'),
        ),
        migrations.AddField(
            model_name='member',
            name='linkedin_link',
            field=models.TextField(blank=True, null=True, verbose_name='Linkedin profile link of this person'),
        ),
        migrations.AddField(
            model_name='member',
            name='working',
            field=models.TextField(blank=True, null=True, verbose_name='working experiences'),
        ),
        migrations.AddField(
            model_name='subteam',
            name='eng_name',
            field=models.CharField(db_index=True, default='eng_name', max_length=50, verbose_name='subteam name'),
        ),
        migrations.AddField(
            model_name='teamadvisor',
            name='did_work',
            field=models.BooleanField(default=False, verbose_name="if True: This person will be shown on 'graduated' pagewith the infos of 'working' and 'eng_working'"),
        ),
        migrations.AlterField(
            model_name='subteam',
            name='leaders',
            field=models.ManyToManyField(blank=True, related_name='leader_of', to='members.Member', verbose_name='subteam leaders'),
        ),
    ]
