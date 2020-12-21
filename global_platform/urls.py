from django.urls import path
from .views import *

urlpatterns =[
#Для варианта с функциями в views.py
    path('', index, name='home' ),

#для варианта с классами в view.py
#    path('', HomeTasks.as_view(), name='home' ),
]