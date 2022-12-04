from django.db import models

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class BaseRank(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ранг, с которого нужен буст'
        verbose_name_plural = 'Ранги, с которых нужен буст'


class DesiredRank(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ранг, до которого нужен буст'
        verbose_name_plural = 'Ранги, до которых нужен буст'


class Product(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    base_rank = models.ForeignKey(BaseRank, on_delete=models.PROTECT)
    desired_rank = models.ForeignKey(DesiredRank, on_delete=models.PROTECT)
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='product_images', verbose_name='Изображение', null=True)
    is_bestseller = models.BooleanField(verbose_name='Бестселлер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
