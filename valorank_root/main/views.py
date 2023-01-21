import os

from django.db.models import Q
from django.views.generic import ListView

from store.models import Product
from articles.models import Article
from users.models import User

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class IndexListView(ListView):
    """
    Представление для рендера главной страницы. Выводит 5 последних статей и 3 бестселлера
    """
    template_name = 'index.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by('-pk')[:5].prefetch_related('category').only(
            'title',
            'category',
            'image'
        )
        context['object_list'] = Product.objects.filter(is_bestseller=True)[:3].only(
            'title',
            'current_price',
            'image'
        )

        return context


class AboutUsListView(ListView):
    """
    Представление для рендера страницы "О нас". Выводит 3 бустера по указанным
    первичным ключам.
    """

    template_name = 'about.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = User.objects.filter(is_best=True).prefetch_related('mailbox').only('avatar', 'mailbox')

        return context
