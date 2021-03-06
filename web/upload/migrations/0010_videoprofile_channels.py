# Generated by Django 2.1.8 on 2019-04-30 09:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('browse', '0007_auto_20190430_1748'),
        ('upload', '0009_remove_videoprofile_channels'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoprofile',
            name='channels',
            field=models.ManyToManyField(blank=True, through='browse.VideoProfileChannelRelation', to='browse.Channel',
                                         verbose_name='チャンネル'),
        ),
    ]
