# Generated by Django 4.0.5 on 2022-08-11 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_video_files_remove_history_video_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='validation',
            name='User_Main',
        ),
    ]
