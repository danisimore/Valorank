from django.views.generic import ListView, TemplateView

from .models import Article

all_articles = Article.objects.all()


class ArticlesListView(ListView):
    """
    Представление для вывода всех статей
    """
    template_name = 'articles.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['updates'] = Article.objects.filter(is_update=True).prefetch_related('category').only(
            'title',
            'creation_date',
            'category',
            'image'
        )
        context['information_and_articles'] = all_articles.exclude(is_update=True).prefetch_related('category').only(
            'title',
            'creation_date',
            'category',
            'image'
        )

        return context


class ArticleDetailView(TemplateView):
    """
    Представление для вывода определенной статьи.
    """
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        selected_article_pk = kwargs['pk']

        context = super().get_context_data(**kwargs)
        context['article'] = Article.objects.filter(pk=selected_article_pk)
        context['other_articles'] = all_articles.exclude(pk=selected_article_pk).order_by('-pk')[:3]

        return context
