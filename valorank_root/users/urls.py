from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from .views import SignUpView, SignInView, EmailVerify

urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path(
        'confirm_email/',
        TemplateView.as_view(template_name='authentication/confirm_email.html'),
        name='confirm_email'
    ),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path(
        'invalid_verify/',
        TemplateView.as_view(template_name='authentication/invalid_verify.html'),
        name='invalid_verify'
    ),
    path(
        'success_verify',
         TemplateView.as_view(template_name='authentication/success_email_verify.html'),
         name='success_email_verify'
    ),
    path('logout/', LogoutView.as_view(), name='logout'),
]
