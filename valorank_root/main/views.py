from django.shortcuts import render
from django.views.generic import ListView
from store.models import Product
from articles.models import Article

class IndexView(ListView):
    template_name = 'index.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by('-pk')[:5]

        return context