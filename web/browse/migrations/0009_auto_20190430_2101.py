# Generated by Django 2.1.8 on 2019-04-30 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('browse', '0008_auto_20190430_2101'),
        ('upload', '0011_auto_20190430_2101'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VideoProfileChannelRelation',
        ),
        migrations.AddField(
            model_name='videoprofilelabelrelation',
            name='label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='browse.Labels'),
        ),
        migrations.AddField(
            model_name='videoprofilelabelrelation',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.VideoProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='videoprofilelabelrelation',
            unique_together={('profile', 'label')},
        ),
    ]
