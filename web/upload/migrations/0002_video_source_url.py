# Generated by Django 2.1.8 on 2019-04-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='source_url',
            field=models.URLField(blank=True, null=True, verbose_name='インポート元URL'),
        ),
    ]
