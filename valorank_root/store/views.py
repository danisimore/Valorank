import re

from django.views.generic import FormView
from .models import Product
from .forms import RankSelectionForm


class StoreFormView(FormView):
    template_name = 'store.html'
    form_class = RankSelectionForm

    def get_context_data(self, **kwargs):
        context = super(StoreFormView, self).get_context_data(**kwargs)

        if ('base_rank' in self.request.get_full_path()) and ('desired_rank' in self.request.get_full_path()):
            url = re.findall('[0-9][0-9]|[0-9]|[0-9][0-9]', self.request.get_full_path())
            context['products_list'] = Product.objects.filter(base_rank=url[0]).filter(desired_rank=url[1])

        return context


