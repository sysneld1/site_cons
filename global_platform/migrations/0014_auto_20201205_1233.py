# Generated by Django 3.0.11 on 2020-12-05 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('global_platform', '0013_auto_20201205_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_actions',
            name='id_task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='global_platform.Tasks', verbose_name='Задача'),
        ),
    ]