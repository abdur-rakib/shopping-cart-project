from django.contrib import admin
from .models import Category, Product, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'discount_price', 'available']
    list_editable = ['price', 'discount_price', 'available']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'created', 'content']