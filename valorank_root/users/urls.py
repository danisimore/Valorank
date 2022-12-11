from django.contrib.auth.views import (
    LogoutView,
    PasswordResetDoneView,
    PasswordResetCompleteView
)
from django.urls import path
from django.views.generic import TemplateView

from . import views

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

urlpatterns = [
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path(
        'confirm_email/',
        TemplateView.as_view(template_name='authentication/confirm_email.html'),
        name='confirm_email'
    ),
    path('verify_email/<uidb64>/<token>/', views.EmailVerify.as_view(), name='verify_email'),
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
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path(
        'password_reset/done',
        PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html'),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'),
        name="password_reset_complete",
    ),
    path('logout/', LogoutView.as_view(), name='logout'),
]
