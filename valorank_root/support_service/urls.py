from django.urls import path
from django.views.generic import TemplateView

from .views import SupportServiceFormView

urlpatterns = [
    path('', SupportServiceFormView.as_view(), name='support_service'),
    path('submission/status', TemplateView.as_view(template_name='submission_status.html'), name='submission_status'),
]