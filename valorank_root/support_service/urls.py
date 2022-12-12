from django.urls import path

from .views import SupportServiceFormView, SubmissionStatusView

urlpatterns = [
    path('', SupportServiceFormView.as_view(), name='support_service'),
    path('submission/status', SubmissionStatusView.as_view(), name='submission_status'),
]