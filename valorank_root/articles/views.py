from django.shortcuts import render
from django.views.generic import ListView

from .models import Article

class ArticleListView(ListView):
    template_name = 'articles.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['updates'] = Article.objects.filter(category=1)
        context['information_and_articles'] = Article.objects.all().exclude(category=1)

        return context