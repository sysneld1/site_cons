# Generated by Django 3.0.11 on 2020-12-04 12:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('global_platform', '0004_remove_specialists_task_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='resolved_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tasks',
            name='description_short',
            field=models.CharField(max_length=300, verbose_name='Короткое описание'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='files',
            field=models.FileField(blank=True, upload_to='files/%Y/%m/%d/', verbose_name='Файлы'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='id_pay',
            field=models.CharField(blank=True, max_length=100, verbose_name='Номер платежа'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='resolved',
            field=models.BooleanField(default=False, verbose_name='Дата решения'),
        ),
    ]
