# Generated by Django 2.1.8 on 2019-04-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('upload', '0005_auto_20190428_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoprofile',
            name='ordered_fps',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='fps'),
        ),
    ]
