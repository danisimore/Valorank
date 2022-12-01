from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    content = models.TextField(verbose_name='Текст статьи')
    image = models.ImageField(upload_to='articles', verbose_name='Изображение')
    video = models.CharField(max_length=500, blank=True, verbose_name='Видео')
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статей'
