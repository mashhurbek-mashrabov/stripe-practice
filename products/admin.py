from django.contrib import admin
from django.contrib.admin import ModelAdmin

from products.models import Product


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']
