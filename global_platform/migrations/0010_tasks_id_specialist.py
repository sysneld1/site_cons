# Generated by Django 3.0.11 on 2020-12-04 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('global_platform', '0009_auto_20201204_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='id_specialist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='global_platform.Specialists'),
        ),
    ]
