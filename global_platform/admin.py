from django.contrib import admin

# Register your models here.

from .models import Clients, Tasks, Payment, Log_actions, Specialists, Category, Thema, Wallet, Log_telnet, Table1, Status


class ClientsAdmin(admin.ModelAdmin):
    list_display =('login','password', 'family', 'name','phone', 'email', 'avatar')
    list_display_links =('login', 'avatar')
    search_fields = ('login', 'name', 'phone', 'email')
    list_editable =('phone',)
    list_filter =('login', 'phone', 'email')


class TasksAdmin(admin.ModelAdmin):
    list_display =('id_client', 'id_specialist', 'description_short', 'status', 'created_at', 'resolved', 'resolved_at',
                 'id_theme', 'id_category', 'payed', 'id_pay', 'files', 'photo')
    list_display_links=('id_client', 'description_short', 'files','created_at', 'resolved')
    search_fields = ('id_client', 'id_specialist', 'files','created_at', 'resolved')

class PaymentAdmin(admin.ModelAdmin):
    list_display =('summa', 'paid', 'data_paid', 'payment_account')
    list_display_links =('summa',)
    search_fields = ('summa', 'paid', 'data_paid', 'payment_account')

class Log_actionsAdmin(admin.ModelAdmin):
    list_display =('id', 'id_task', 'created_at', 'text', 'files', 'images', 'id_executor', 'id_client', 'id_specialist')
    list_dislplay_links =('id','id_task', 'files', 'id_executor', 'id_client', 'id_specialist')
    search_fields = ('id', 'id_task', 'text',  'id_executor', 'id_client', 'id_specialist')


class SpecialistsAdmin(admin.ModelAdmin):
    list_display=('login', 'password', 'family', 'name', 'phone', 'email', 'payment_invoice',
        'self_qualification', 'self_experience', 'real_experience', 'real_qualification', 'real_speed', 'real_quality', 'real_cost', 'avatar')
    list_display_links = ('login', 'password', 'family', 'name', 'phone', 'email', 'payment_invoice')
    search_fields = ('login', 'password', 'family', 'name', 'phone', 'email',  'payment_invoice')

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id_thema', 'title', 'description')
    list_dislplay_links=('id_thema', 'title')
    search_fields =('id_thema', 'title', 'description')




class ThemaAdmin(admin.ModelAdmin):
    list_display= ('id', 'title', 'description')
    list_display_links = ('id','title', 'description')
    search_fields =('title', 'description')




class WalletAdmin(admin.ModelAdmin):
    list_dislplay =('id_specialist', 'summa')
    list_dislplay_links = ('id_specialist', 'summa')
    search_fields = ('id_specialist', 'summa')


class Log_telnetAdmin(admin.ModelAdmin):
    list_display =('id_task', 'created_at', 'text', 'files', 'images', 'id_executor', 'id_client', 'id_specialist')
    list_dislplay_links = ('id_task', 'created_at', 'text', 'files', 'images', 'id_executor', 'id_client', 'id_specialist')
    search_fields =('id_task', 'created_at', 'text', 'files', 'images', 'id_executor', 'id_client', 'id_specialist')

class StatusAdmin(admin.ModelAdmin):
    list_display=('id', 'status_title')
    list_dislplay_links=('id', 'status_title')



admin.site.register(Clients, ClientsAdmin)
admin.site.register(Tasks, TasksAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Log_actions, Log_actionsAdmin)
admin.site.register(Specialists, SpecialistsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Thema, ThemaAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(Log_telnet, Log_telnetAdmin)
admin.site.register(Status, StatusAdmin)

