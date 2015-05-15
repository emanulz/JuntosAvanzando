# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from models import Cliente, Asociado


@admin.register(Cliente)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'identification', 'adress', 'email', 'phone_number', 'hascredit')
    # list_filter = ('name','identification')
    search_fields = ('name', 'identification', 'last_name', )

    def hascredit(self, obj):
        return obj.credit

    hascredit.admin_order_field = 'credit'
    hascredit.boolean = True
    hascredit.short_description = "Tiene crédito?"

@admin.register(Asociado)
class AsociadoAdmin(admin.ModelAdmin):
    list_display = ('id','name','afiliate_code')