# Generated by Django 3.0.11 on 2020-12-04 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('global_platform', '0005_auto_20201204_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='id_theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='global_platform.Thema', verbose_name='Тема'),
        ),
    ]
