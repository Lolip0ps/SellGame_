from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    list_display_links = ('id', 'email')
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)


# admin.site.register(OrderItem)

