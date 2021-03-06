# Generated by Django 3.0.11 on 2020-12-04 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_platform', '0002_auto_20201204_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialists',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatar/%Y/%m/%d/', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='specialists',
            name='family',
            field=models.CharField(blank=True, max_length=20, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='specialists',
            name='name',
            field=models.CharField(blank=True, max_length=20, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='specialists',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Телефон'),
        ),
    ]
