import re

from django.views.generic import FormView

from .models import Product
from .forms import RankSelectionForm



class StoreFormView(FormView):
    """
    Представление для рендера страницы магазина.
    """

    template_name = 'store.html'
    form_class = RankSelectionForm

    def get_context_data(self, **kwargs):
        context = super(StoreFormView, self).get_context_data(**kwargs)

        """
        Когда пользователь выбирает base_rank и desired_rank, url выглядит примерно так:
            /store/?base_rank=1&desired_rank=1#
            
        Регулярное выражение ищет все числа в url. Сначала находит base_rank= --> 1 <-- и забирает 1,
        затем тоже самое делает и с desired_rank. В итоге получается список из двух элементов, в пером индексе
        которого хранится base_rank.pk, во втором, соответственно desired_rank.pk. Далее в контекст передается
        продукт, у которого base_rank и desired_rank равны найденным элементам в запросе.
        """
        if ('base_rank' in self.request.get_full_path()) and ('desired_rank' in self.request.get_full_path()):
            url = re.findall('[0-9][0-9]|[0-9]|[0-9][0-9]', self.request.get_full_path())
            context['products_list'] = Product.objects.filter(base_rank=url[0]).filter(desired_rank=url[1])

        return context

