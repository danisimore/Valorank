from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Article, ArticleCategory


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(label='Текст статьи', widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'get_image',
        'creation_date',
    )
    list_display_links = ('id', 'title')
    form = ArticleAdminForm
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

@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
