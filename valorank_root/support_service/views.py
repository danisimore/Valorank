from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView

from .forms import RequestForm


class SupportServiceFormView(FormView):
    """Форма рендера страницы поддержки и отправки запроса"""

    template_name = 'support_service.html'
    form_class = RequestForm

    def post(self, request, *args, **kwargs):
        form = RequestForm(request.POST, request.GET)

        if form.is_valid():
            form.save()
            return redirect('submission_status')
        else:
            return render(request, 'submission_status.html', {'error': 'Форма заполнена некорректно, попробуйте еще раз'})
