from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Article

class ArticlesListView(ListView):
    template_name = 'articles.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['updates'] = Article.objects.filter(category=1)
        context['information_and_articles'] = Article.objects.all().exclude(category=1)

        return context

class ArticleDetailView(TemplateView):
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        selected_article_pk = kwargs['pk']

        context = super().get_context_data(**kwargs)
        context['article'] = Article.objects.filter(pk=selected_article_pk)
        context['other_articles'] = Article.objects.all().exclude(pk=selected_article_pk).order_by('-pk')[:3]


        return context