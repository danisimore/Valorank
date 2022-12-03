from django.contrib import admin
from .models import BaseRank, DesiredRank, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'base_rank', 'desired_rank', 'price')
    list_display_links = ('id',)
    search_fields = ('id', 'base_rank', 'desired_rank')
    list_filter = ('base_rank', 'desired_rank', 'price')
    list_editable = ('title', 'base_rank', 'desired_rank', 'price')
    list_per_page = 10
    list_max_show_all = 100


class BaseRankAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id',)
    search_fields = ('title',)
    list_filter = ('title',)
    list_editable = ('title',)
    list_per_page = 10
    list_max_show_all = 100


class DesiredRankAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id',)
    search_fields = ('title',)
    list_filter = ('title',)
    list_editable = ('title',)
    list_per_page = 10
    list_max_show_all = 100


admin.site.register(Product, ProductAdmin)
admin.site.register(BaseRank, BaseRankAdmin)
admin.site.register(DesiredRank, DesiredRankAdmin)
