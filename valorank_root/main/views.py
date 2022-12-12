from django.db.models import Q
from django.views.generic import ListView

from store.models import Product
from articles.models import Article
from users.models import User


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class IndexListView(ListView):
    template_name = 'index.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by('-pk')[:5]
        context['object_list'] = Product.objects.filter(is_bestseller=True)[:3]

        return context

class AboutUsListView(ListView):
    template_name = 'about.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = User.objects.filter(Q(pk=1)|Q(pk=2)|Q(pk=3))

        return context