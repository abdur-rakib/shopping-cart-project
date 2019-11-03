from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'country', 'created', 'updated', 'paid']
    list_filter = ['created', 'updated', 'paid']
    inlines = [OrderItemInline]