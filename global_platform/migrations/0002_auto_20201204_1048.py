# Generated by Django 3.0.11 on 2020-12-04 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('global_platform', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='task_num',
        ),
        migrations.AlterField(
            model_name='category',
            name='id_thema',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='global_platform.Thema', verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatar/%Y/%m/%d/', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='family',
            field=models.CharField(blank=True, max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='thema',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Тема'),
        ),
    ]