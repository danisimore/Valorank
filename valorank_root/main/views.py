from django.shortcuts import render
from django.views.generic import ListView

from rest_framework.generics import ListAPIView

from store.models import Product
from articles.models import Article
from .serializers import MainPageProductsSerializer, MainPageArticlesSerializer

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

bestsellers = Product.objects.filter(is_bestseller=True)[:3]
last_five_articles = Article.objects.all().order_by('-pk')[:5]


class HomePageProductsView(ListAPIView):
    serializer_class = MainPageProductsSerializer

    def get_queryset(self):
        products = bestsellers
        return products


class HomePageArticles(ListAPIView):
    serializer_class = MainPageArticlesSerializer

    def get_queryset(self):
        articles = last_five_articles
        return articles


class IndexView(ListView):
    template_name = 'index.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = last_five_articles
        context['object_list'] = bestsellers

        return context
