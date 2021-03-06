# Generated by Django 3.0.11 on 2020-12-04 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_platform', '0006_auto_20201204_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='description_short',
            field=models.CharField(max_length=300, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='resolved',
            field=models.BooleanField(default=False, verbose_name='Решена'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='resolved_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата Решения'),
        ),
    ]
