from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'is_published', 'time_create']
    list_filter = ['is_published', 'time_create']
    list_editable = ['price', 'is_published']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


class NameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(NameGame, NameAdmin)


class KeyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'key']


admin.site.register(KeyGame, KeyAdmin)
