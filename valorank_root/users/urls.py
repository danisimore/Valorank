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
    path('logout/', LogoutView.as_view(), name='logout'),

    # email confirm urls
    path(
        'confirm_email/',
        TemplateView.as_view(template_name='authentication/verify_email/confirm_email.html'),
        name='confirm_email'
    ),
    path('verify_email/<uidb64>/<token>/', views.EmailVerify.as_view(), name='verify_email'),
    path(
        'invalid_verify/',
        TemplateView.as_view(template_name='authentication/verify_email/invalid_verify.html'),
        name='invalid_verify'
    ),
    path(
        'success_verify',
        TemplateView.as_view(template_name='authentication/verify_email/success_email_verify.html'),
        name='success_email_verify'
    ),

    # password reset urls
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path(
        'password_reset/done',
        PasswordResetDoneView.as_view(template_name='authentication/password_reset/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(
            template_name='authentication/password_reset/password_reset_confirm.html'),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(template_name='authentication/password_reset/password_reset_complete.html'),
        name="password_reset_complete",
    ),

    # email change urls
    path('email_change/', views.EmailChangeView.as_view(), name='email_change'),
    path(
        'email_change/sent',
        TemplateView.as_view(template_name='authentication/email_change/email_change_sent.html'),
        name='email_change_sent'
    ),
    path('email_change/<uidb64>/<token>/', views.ChangeEmailConfirm.as_view(), name='email_change_confirm'),
    path('email_change/new_email/verify/<uidb64>/<token>/', views.NewEmailVerifyView.as_view(),
         name='new_email_verify'),
    path(
        'email_change/success',
        TemplateView.as_view(template_name='authentication/email_change/success_email_change.html'),
        name='success_email_change'
    ),
    path(
        'email_change/invalid_verify',
        TemplateView.as_view(template_name='authentication/email_change/invalid_new_email_verify.html'),
        name='invalid_new_email_verify'
    ),

    # password change urls
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path(
        'password_change/done',
        TemplateView.as_view(template_name='authentication/password_change/password_change_done.html'),
        name='password_change_done'
    )
]
