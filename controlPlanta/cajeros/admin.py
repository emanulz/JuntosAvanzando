from django.contrib import admin
from models import Cajero

# Register your models here.
@admin.register(Cajero)
class CajeroAdmin(admin.ModelAdmin):
    list_display = ('name','last_name','usernam')
