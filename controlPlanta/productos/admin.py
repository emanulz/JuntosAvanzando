from django.contrib import admin

# Register your models here.
from models import FamiliaDelProducto, Producto



@admin.register(Producto)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_code','bar_code','description','price','category')
    search_fields = ('product_code', 'description', 'bar_code', 'category')

@admin.register(FamiliaDelProducto)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('id','name')