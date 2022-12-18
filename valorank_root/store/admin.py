from django.contrib import admin
from .models import BaseRank, DesiredRank, Product, Order

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'base_rank',
        'desired_rank',
        'discount',
        'current_price',
        'old_price',
        'is_bestseller'
    )
    list_display_links = ('id',)
    search_fields = ('id', 'base_rank', 'desired_rank', 'discount')
    list_filter = ('base_rank', 'desired_rank', 'current_price')
    list_editable = ('title', 'base_rank', 'desired_rank', 'discount', 'current_price', 'old_price', 'is_bestseller')
    list_per_page = 10
    list_max_show_all = 100

@admin.register(BaseRank)
class BaseRankAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id',)
    search_fields = ('title',)
    list_filter = ('title',)
    list_editable = ('title',)
    list_per_page = 10
    list_max_show_all = 100

@admin.register(DesiredRank)
class DesiredRankAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id',)
    search_fields = ('title',)
    list_filter = ('title',)
    list_editable = ('title',)
    list_per_page = 10
    list_max_show_all = 100

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user', 'created_at')
    list_display_links = ('id', 'product')
    search_fields = ('id', 'user', 'product')
    list_filter = ('id', 'created_at')
    list_per_page = 10
    list_max_show_all = 100
