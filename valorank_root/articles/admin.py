from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Article, ArticleCategory


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'get_image',
        'creation_date',
    )
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_filter = ('id', 'title', 'creation_date')
    list_per_page = 10
    list_max_show_all = 100

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50px"')
        else:
            return 'Нет изображения'

    get_image.short_description = 'Изображение'


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory)
