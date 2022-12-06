from django.views.generic import ListView, TemplateView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, ArticleCategory
from .serializers import ArticleSerializer, ArticleCategorySerializer, ArticleDetailSerializer


all_articles = Article.objects.all()

class ArticlesListView(ListView):
    template_name = 'articles.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['updates'] = Article.objects.filter(category=1)
        context['information_and_articles'] = all_articles.exclude(category=1)

        return context

class ArticleDetailView(TemplateView):
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        selected_article_pk = kwargs['pk']

        context = super().get_context_data(**kwargs)
        context['article'] = Article.objects.filter(pk=selected_article_pk)
        context['other_articles'] = all_articles.exclude(pk=selected_article_pk).order_by('-pk')[:3]


        return context

class ArticlesAPIView(ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        articles = all_articles

        return articles

class ArticleCategoriesAPIView(ListAPIView):
    serializer_class = ArticleCategorySerializer

    def get_queryset(self):
        categories = ArticleCategory.objects.all()

        return categories

class ArticleDetailAPIView(APIView):

    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        serializer = ArticleDetailSerializer(article)

        return Response(serializer.data)