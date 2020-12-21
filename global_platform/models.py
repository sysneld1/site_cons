from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Clients(models.Model):
    login =models.CharField(max_length=50, db_index=True, verbose_name = 'Логин')
    password = models.CharField(max_length=15, verbose_name = 'Пароль')
    family = models.CharField(max_length=50, blank=True, verbose_name = 'Фамилия')
    name = models.CharField(max_length=50, blank=True, verbose_name = 'Имя')
    phone = models.CharField(max_length=15, verbose_name = 'Телефон')
    email = models.EmailField(max_length=50,verbose_name = 'E-mail')
#    task_num = models.IntegerField(verbose_name = 'Номер задачи')
    avatar = models.ImageField(blank=True, upload_to='avatar/%Y/%m/%d/', verbose_name = 'Аватар')

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering =['login']

class Tasks(models.Model):
    id_client = models.ForeignKey('Clients', on_delete=models.PROTECT, null=True)
    id_specialist = models.ForeignKey('Specialists', on_delete=models.PROTECT, null=True)
    description_short = models.CharField(max_length=300, verbose_name = 'Краткое описание')
    description_full = models.TextField(verbose_name = 'полное описание')
    files = models.FileField(blank=True, upload_to='files/%Y/%m/%d/', verbose_name = 'Файлы')
    photo = models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name = 'Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата создания')
    resolved = models.BooleanField(default=False, verbose_name = 'Решена')
    status = models.ForeignKey('Status', on_delete=models.PROTECT, verbose_name='Статус', null=True)
    resolved_at= models.DateTimeField(blank=True, null=True,  verbose_name = 'Дата Решения')
    payed = models.BooleanField(default=False, verbose_name = 'Оплачено')
    id_pay=models.CharField(blank=True, max_length=100, verbose_name = 'Номер платежа')
    id_theme=models.ForeignKey('Thema', verbose_name= 'Тема', on_delete=models.PROTECT)
    id_category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT)

    def __str__(self):
        return (str(self.id)+' '+str(self.description_short))

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering =['id_client']

class Payment(models.Model):
    id_task = models.ForeignKey('Tasks', on_delete=models.PROTECT, null=True)
    summa = models.FloatField(verbose_name = 'Сумма')
    paid = models.BooleanField(default=False, verbose_name='Оплачено')
    data_paid = models.DateTimeField(auto_now_add=True, verbose_name='Дата платежа')
    payment_account=models.CharField(max_length=30, verbose_name = 'номер счета')

    def __str__(self):
        return self.id_task

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering =['id_task']

class Log_actions(models.Model):
    id_task =models.ForeignKey('Tasks', on_delete = models.PROTECT, null=True, verbose_name = 'Задача')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата создания')
    text = models.TextField(blank=True, verbose_name = 'Сообщение')
    files = models.FileField(blank=True, upload_to ='log_files/%Y/%m/%d/', verbose_name = 'файл активности')
    images = models.ImageField(blank=True, upload_to = 'log_images/%Y/%m/%d/', verbose_name = 'Изображение активности')
    id_executor = models.CharField(blank=True, max_length=150, verbose_name ='На кого назначена')
    id_client =models.ForeignKey('Clients', verbose_name = 'Клиент',  on_delete= models.PROTECT, null=True)
    id_specialist = models.ForeignKey('Specialists', verbose_name ='специалист', on_delete= models.PROTECT, null=True)

    def __str__(self):
        return str(self.id_task)

    class Meta:
        verbose_name = 'Действие по задаче'
        verbose_name_plural = 'Действия по задаче'
        ordering =['id_task']


class Specialists(models.Model):
    login = models.CharField(max_length=20, verbose_name= 'Логин')
    password =models.CharField(max_length=20, verbose_name = 'Пароль')
    family = models.CharField(max_length=20, blank=True, verbose_name = 'Фамилия')
    name = models.CharField(max_length=20, blank=True, verbose_name = 'Имя')
    phone = models.CharField(max_length=15, verbose_name = 'Телефон')
    email = models.EmailField(max_length=50,verbose_name = 'E-mail')
#    task_num = models.IntegerField(verbose_name = 'Номер задачи')
    avatar = models.ImageField(blank=True, upload_to='avatar/%Y/%m/%d/', verbose_name = 'Аватар')
    payment_invoice=models.CharField(max_length=40, verbose_name ='Номер счета')
    self_qualification = models.IntegerField(validators=[MaxValueValidator(100)],  verbose_name ='Квалификация')
    self_experience = models.IntegerField(validators=[MaxValueValidator(100)], verbose_name = 'Опыт')
    real_qualification =models.IntegerField(validators=[MaxValueValidator(100)], verbose_name ='Реальная Квалификация')
    real_experience = models.IntegerField(validators=[MaxValueValidator(100)], verbose_name = 'Реальный Опыт')
    real_quality=models.IntegerField(validators=[MaxValueValidator(100)], verbose_name = 'Реальный качество')
    real_speed =models.IntegerField(validators=[MaxValueValidator(100)], verbose_name = 'Реальная скорость')
    real_cost = models.IntegerField(validators=[MaxValueValidator(100)], verbose_name = 'Адекватность цены')

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'
        ordering =['login']


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name= 'Катергоия')
    description =models.TextField(blank=True, verbose_name= 'Описание')
    id_thema =models.ForeignKey('Thema', on_delete = models.PROTECT, null=True, verbose_name='Тема')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering =['title']


class Thema(models.Model):
    title = models.CharField(max_length=150, verbose_name= 'Тема')
    description =models.TextField(blank=True, verbose_name= 'Описание')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering =['title']


class Wallet(models.Model):
    id_specialist= models.ForeignKey('Specialists', on_delete = models.PROTECT, null=True)
    summa =models.IntegerField(verbose_name = 'Сумма')

    def __str__(self):
        return self.id_specialist

    class Meta:
        verbose_name = 'Кошелек'
        verbose_name_plural = 'Кошельки'
        ordering =['id_specialist']



class Log_telnet(models.Model):
    id_task =models.ForeignKey('Tasks', on_delete = models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата создания')
    text = models.TextField(blank=True, verbose_name = 'Сообщение')
    files = models.FileField(upload_to ='log_files/%Y/%m/%d/', verbose_name = 'файл активности')
    images = models.ImageField(upload_to = 'log_images/%Y/%m/%d/', verbose_name = 'Изображение активности')
    id_executor = models.IntegerField(verbose_name ='На кого назначена')
    id_client =models.IntegerField(verbose_name = 'Клиент')
    id_specialist = models.IntegerField(verbose_name = 'Специалист')

    def __str__(self):
        return self.id_task

    class Meta:
        verbose_name = 'Действие в telnet'
        verbose_name_plural = 'Действия в telnet'
        ordering =['id_task']


class Table1(models.Model):
    field1 = models.ForeignKey('Clients', on_delete=models.PROTECT, null=True)
    field2 = models.CharField(max_length=150, verbose_name = 'Короткое описание')
    field3 = models.TextField(verbose_name = 'полное описание')
    field4 = models.FileField(upload_to='files/%Y/%m/%d/', verbose_name = 'Файлы')
    field5 = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name = 'Фото')
    field6 = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата создания')
    field7 = models.BooleanField(default=False, verbose_name = 'Решена')
    field8 = models.BooleanField(default=False, verbose_name = 'Оплачено')
    field9 = models.CharField(max_length=150, verbose_name = 'Номер платежа')
    field10 = models.IntegerField(verbose_name= 'Тема')
    field11 = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.field1

    class Meta:
        verbose_name = 'Таблица1 резерв'
        verbose_name_plural = 'Таблицы1 резерв'
        ordering =['field1']


class Status(models.Model):
    status_title  =models.CharField(max_length=150, verbose_name = 'Статус')

    def __str__(self):
        return self.status_title

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering =['status_title']


