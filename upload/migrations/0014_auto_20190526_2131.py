# Generated by Django 2.1.8 on 2019-05-26 12:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('upload', '0013_auto_20190430_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='type',
            field=models.CharField(choices=[('normal', '通常投稿'), ('updated', '通常投稿(再投稿済み)'), ('twitter', 'ツイッターからインポート'),
                                            ('altwug', 'Altwugからインポート')], default='normal', max_length=20,
                                   verbose_name='動画タイプ'),
        ),
    ]
