from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.tokens import default_token_generator as token_generator

from django.contrib.auth.views import (
    LoginView,
    PasswordResetView as DjangoPasswordResetView,
    PasswordResetConfirmView as DjangoPasswordResetConfirmView,
    PasswordChangeView as DjangoPasswordChangeView
)

from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.generic import FormView

from . import forms
from .utils import send_email_for_verify

User = get_user_model()

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''                                               Login/Register Views                                               '''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class SignInView(LoginView):
    """
    Представление для авторизации пользователя
    """

    template_name = 'authentication/signin.html'
    form_class = forms.LoginForm


class SignUpView(View):
    """
    Представление для регистрации пользователя. Если метод POST и форма валидна,
    пользователя перенаправляет на страницу подтверждения почты. Если форма не валидна,
    то в контекст передается форма, и происходит рендер этой же страницы.
    """

    template_name = 'authentication/signup.html'

    def get(self, request):
        context = {
            'form': forms.CreateUser()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = forms.CreateUser(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            send_email_for_verify(request, user, 'authentication/verify_email/verify_email.html', user.email)
            return redirect('confirm_email')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''                                                Email Verify View                                                 '''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class EmailVerify(View):
    """
    Представление верификации почты. Функция get_user расшифровывает uidb64
    и пытается найти пользователя с pk, равному расшифрованному значению.
    Если пользователь найден, а также токен, совпадает с ним, то поле email_verify выставляется в True и
    пользователя авторизует. Если данные результата расшифровки ссылки невалидны,
    то происходит redirect на соответствующую страницу.
    """

    def get(self, request, uidb64, token):

        user = self.get_user(uidb64)
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


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''                                               Password Reset Views                                               '''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class PasswordResetView(DjangoPasswordResetView):
    """
    Представление для сброса пароля. Унаследовано от базового класса сброса пароля Django.
    Переопределена форма и шаблоны.
    """
    email_template_name = 'authentication/password_reset/password_reset_email.html'
    template_name = 'authentication/password_reset/password_reset_form.html'
    form_class = forms.PasswordResetForm


class PasswordResetConfirmView(DjangoPasswordResetConfirmView):
    """
    Представление для ввода нового пароля при сбросе. Унаследовано от базового класса сброса пароля Django.
    Переопределена форма и шаблоны.
    """
    template_name = 'authentication/password_reset/password_reset_confirm.html'
    form_class = forms.SetPasswordForm


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''                                                Email Change Views                                                '''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class EmailChangeView(FormView):
    """
    Представление для смены почты. Форма требует ввода текущей почты.
    Если почта валидна, то на нее отправляется письмо со ссылкой на
    ввод новой почты. Если форма не валидна,
    то выводятся соответствующие ошибки. На самом деле письмо содержит
    ссылку на url, за который отвечает представление ChangeEmailConfirmCheckUrl.
    Его описание можно найти ниже.
    """

    form_class = forms.EmailChangeForm
    template_name = 'authentication/email_change/email_change.html'

    def form_valid(self, form):
        if form.cleaned_data.get('email') == self.request.user.email:
            send_email_for_verify(
                self.request,
                self.request.user,
                'authentication/email_change/email_for_email_change.html',
                self.request.user.email
            )

            return redirect('email_change_sent')
        else:
            form.add_error(None, 'Кажется вы ввели некорректный адрес электронной почты. '
                                 'Пожалуйста, введите свой текущий адрес электронной почты и попробуйте еще раз')
            return render(self.request, 'authentication/email_change/email_change.html', {'form': form})


class ChangeEmailConfirmCheckUrl(View):
    """
    Это представление проверяет, совпадает ли url, по которому перешел пользователь,
    с отправленным ему на почту путем получения из него uidb64, его расшифровки и проверки токена.
    Аналогично EmailVerify, который описан выше.
    Если совпадает, то происходит redirect на страницу смены почты.
    """

    def get(self, request, uidb64, token):

        user = self.get_user(uidb64)
        if user is not None and token_generator.check_token(user, token):
            return redirect('email_change_confirm')
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


class ChangeEmailConfirm(FormView):
    """
    На url, за который отвечает это представление, пользователь попадает в случае
    успешной проверки ChangeEmailConfirmCheckUrl. Форма содержит поля для ввода
    новой почты. Если у пользователя уже есть temporary_email, то он удаляется,
    а далее в это поле записывается только что введенное значение. В случае
    отсутствия temporary_email, оно просто записывается ничего не удаляя.
    Далее, на temporary_email пользователю отправляется письмо с верификацией и
    происходит redirect на страницу с оповещением о том, что письмо было
    отправлено.
    """

    form_class = forms.TemporaryEmailForm
    template_name = 'authentication/email_change/email_change_confirm.html'

    def form_valid(self, form):
        if self.request.user.temporary_email:
            User.objects.filter(pk=self.request.user.pk).update(temporary_email=None)
            User.objects.filter(pk=self.request.user.pk).update(
                temporary_email=form.cleaned_data.get('temporary_email'))
        else:
            User.objects.filter(pk=self.request.user.pk).update(
                temporary_email=form.cleaned_data.get('temporary_email'))

        send_email_for_verify(
            self.request,
            self.request.user,
            'authentication/email_change/new_email_verify.html',
            self.request.user.temporary_email
        )

        return redirect('confirm_email')

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


class NewEmailVerifyView(View):
    """
    Представление для проверки валидности url, по которому пользователь
    пытается подтвердить новый email. Проверка осуществляется аналогично тому,
    как и в EmailVerify или ChangeEmailConfirmCheckUrl. Если данные из url валидны,
    то пользователя перенаправляет на страницу с оповещением об успешной смене почты.
    Иначе на страницу с оповещением об неудачной смене почты.
    """
    def get(self, request, uidb64, token):

        user = self.get_user(uidb64)
        if user is not None and token_generator.check_token(user, token) and not User.objects.filter(
                email=user.temporary_email):
            user.email = user.temporary_email
            user.temporary_email = None
            user.save()
            return redirect('success_email_change')
        else:
            user.temporary_email = None
            return redirect('invalid_new_email_verify')

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


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''                                               Password Change View                                               '''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class PasswordChangeView(DjangoPasswordChangeView):
    """
    Представление смены пароля. Унаследовано от базового класса смены пароля Django.
    Переопределены: шаблон, success_url и форма.
    """


    template_name = 'authentication/password_change/password_change_form.html'
    success_url = reverse_lazy("password_change_done")
    form_class = forms.PasswordChangeForm
