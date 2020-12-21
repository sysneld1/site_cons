from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError


class TaskForm(forms.ModelForm):
    class Meta :
        model = Tasks
    #    fields = '__all__'
        fields = ['description_short', 'description_full', 'files', 'photo', 'resolved', 'id_theme', 'id_category']
        widgets ={
           'description_short': forms.TextInput(attrs={"class": "form-control"}),
           'description_full' : forms.Textarea(
              attrs={
                "class": "form-control",
                "rows": 10}),
            'id_theme': forms.Select(attrs={"class": "form-control"}),
            'id_category' : forms.Select(attrs={"class": "form-control"})
        }

#Проверяем для примера, что поле не начинается на цифру - тест
    def clean_description_short(self):
  #получаем чистые данные - строка с длинной не более 150
        description_short=self.cleaned_data['description_short']
 #Проверяем есть ли цифра вначале
        if re.match(r'\d', description_short):
            raise ValidationError('Название не должно начинаться с цифры')
        return description_short

    '''
class TaskForm(forms.Form):

    description_short = forms.CharField(max_length=300,  label='Краткое описание', widget=forms.TextInput(attrs={"class": "form-control"}))
    description_full = forms.CharField(label='Полное описание', widget=forms.Textarea(
      attrs={
       "class": "form-control",
        "rows": 10}))
    files = forms.FileField(required=False, label='Файл')
    photo = forms.ImageField(required=False, label='Изображение')
    resolved = forms.BooleanField(required=False, label='Решена')
    id_theme = forms.ModelChoiceField(empty_label='Выберете тему', queryset=Thema.objects.all(),label='Тема',
     widget=forms.Select(attrs={"class": "form-control"}))

    id_category = forms.ModelChoiceField(empty_label='Выберете категорию', queryset=Category.objects.all(),label='Категория',
     widget=forms.Select(attrs={"class": "form-control"}))
    '''

    '''
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
    id_category = models.ForeignKey('Category', on_delete=models.PROTECT)
    '''
