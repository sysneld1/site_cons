from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from django.http import HttpResponse
from .models import *
from .forms import TaskForm

#Вариант через класс
class HomeTasks(ListView):
    model =Tasks
    template_name = 'tasks/home_tasks_list.html'
    context_object_name = 'tasks'
    extra_context = {'title': '!Главная!'}
#чтобы переопределить данные
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'главная страница'
#Чтобы выводить не все данные - а с фильром
    def get_queryset(self):
#Отображать решенные
        return Tasks.objects.filter(resolved=True)


#Вариант через функции
def index(request):
    print(request)
    res = '<h1>Задачи</h1>'
    tasks= Tasks.objects.order_by('-id')
#    for item in tasks:
#        res += f'<div>\n<p>{item.id}</p>\n<p>{item.description_short}</p>\n<p>{item.description_full}</p>\n</div>\n<hr>\n'
#    return HttpResponse(res)[<0;77;15M

    if request.method== 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
        #    print(form.cleaned_data)
        #    tasks= Tasks.objects.create(**form.cleaned_data)
            tasks = form.save()
        #    return redirect('home')
            return redirect (tasks)
    else:
        form = TaskForm()

    context = {
        'tasks': tasks, 
        'title': 'Список задач',
        'form' : form
        }
    return render(request, 'global_platform/index.html', context)

#    return render(request, 'global_platform/base.html', context)