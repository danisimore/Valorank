from django.db import models
from users.models import User

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
    """
    :old_price: Указывать, если discount = True
    """

    title = models.CharField(max_length=256, verbose_name='Название')
    base_rank = models.ForeignKey(BaseRank, on_delete=models.PROTECT)
    desired_rank = models.ForeignKey(DesiredRank, on_delete=models.PROTECT)
    discount = models.BooleanField(verbose_name='Товар со скидкой', blank=True, default=False)
    old_price = models.IntegerField(verbose_name='Старая цена', blank=True, null=True)
    current_price = models.IntegerField(verbose_name='Текущая цена')
    execution_time = models.CharField(max_length=128, verbose_name='Время выполнения', blank=True)
    image = models.ImageField(upload_to='product_images', verbose_name='Изображение', blank=True)
    is_bestseller = models.BooleanField(verbose_name='Бестселлер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT, verbose_name='Продукт')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __int__(self):
        return self.pk

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'