# Generated by Django 3.0.11 on 2020-12-04 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_platform', '0007_auto_20201204_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='resolved_at',
            field=models.DateTimeField(blank=True, verbose_name='Дата Решения'),
        ),
    ]
