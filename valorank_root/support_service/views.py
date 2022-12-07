from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView

from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import RequestForm
from .serializers import SupportRequestSerializer

class SubmissionStatusView(TemplateView):
    template_name = 'submission_status.html'



class SupportServiceFormView(FormView):
    template_name = 'support_service.html'
    form_class = RequestForm

    def post(self, request, *args, **kwargs):
        form = RequestForm(request.POST, request.GET)

        if form.is_valid():
            form.save()
            return redirect('submission_status')
        else:
            return render(request, 'submission_status.html', {'error': 'Форма заполнена некорректно, попробуйте еще раз'})

class SupportServiceAPIView(APIView):

    def post(self, request):
        support_request = SupportRequestSerializer(data=request.data)
        if support_request.is_valid():
            support_request.save()
        return Response(status=201)