# Generated by Django 2.1.7 on 2019-03-19 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('ajax', '0003_point_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='IPアドレス'),
        ),
        migrations.AlterField(
            model_name='point',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
    ]