from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.auth.views import (
    LoginView,
    PasswordResetView as DjangoPasswordResetView,
    PasswordResetConfirmView as DjangoPasswordResetConfirmView
)
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.generic import FormView

from .forms import LoginForm, CreateUser, PasswordResetForm, SetPasswordForm
from .utils import send_email_for_verify

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

User = get_user_model()


class SignInView(LoginView):
    template_name = 'authentication/signin.html'
    form_class = LoginForm


class SignUpView(View):
    template_name = 'authentication/signup.html'

    def get(self, request):
        context = {
            'form': CreateUser()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CreateUser(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            send_email_for_verify(request, user, 'authentication/verify_email.html', user.email)
            return redirect('confirm_email')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class EmailVerify(View):
    def get(self, request, uidb64, token):

        user = self.get_user(uidb64)
        print(user)
        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('success_email_verify')
        else:
            return redirect('invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (
                TypeError,
                ValueError,
                OverflowError,
                User.DoesNotExist,
                ValidationError,
        ):
            user = None
        return user



class PasswordResetView(DjangoPasswordResetView):
    email_template_name = 'authentication/password_reset_email.html'
    template_name = 'authentication/password_reset_form.html'
    form_class = PasswordResetForm


class PasswordResetConfirmView(DjangoPasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirm.html'
    form_class = SetPasswordForm

