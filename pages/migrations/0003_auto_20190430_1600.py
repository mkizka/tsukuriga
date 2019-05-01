# Generated by Django 2.1.8 on 2019-04-30 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('pages', '0002_page_featured_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='author',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL,
                                    verbose_name='筆者'),
        ),
    ]