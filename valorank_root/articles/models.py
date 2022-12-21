from django.db import models

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class ArticleCategory(models.Model):
    """
    :css: Необходим для отображения фона категории статьи. Может быть bg-danger или bg-info.
    """

    title = models.CharField(max_length=128, verbose_name='Название')
    css = models.CharField(max_length=128, verbose_name='CSS-класс', default='bg-danger')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Article(models.Model):
    """
    :video: Формат ссылки для корректной работы должен быть: https://www.youtube.com/embed/9sQH927Y7m4?controls=1 .
            Т.е. обычная ссылка выглядит так: https://www.youtube.com/watch?v=9sQH927Y7m4&ab_channel=LofiAngel.
            Вы должны привести ее к виду первого варианта.
    """
    title = models.CharField(max_length=256, verbose_name='Название')
    content = models.TextField(verbose_name='Текст статьи')
    image = models.ImageField(upload_to='articles', verbose_name='Изображение')
    video = models.CharField(max_length=500, blank=True, verbose_name='Видео')
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, blank=True, null=True)
    is_update = models.BooleanField(default=False)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'
