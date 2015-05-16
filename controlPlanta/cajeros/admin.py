from django.contrib import admin
from models import Cajero

# Register your models here.
@admin.register(Cajero)
class CajeroAdmin(admin.ModelAdmin):
    list_display = ('id','name','last_name','identification','user')
    search_fields = ('id', 'name', 'identification', 'user')