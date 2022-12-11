from django.contrib.auth import get_user_model, password_validation, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django import forms

from users.utils import send_email_for_verify


class CreateUser(UserCreationForm):
    email = forms.CharField(
        label=_(''),
        widget=forms.EmailInput(attrs={"placeholder": "Введите Email"})
    )

    password1 = forms.CharField(
        label=_(""),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder": "Введите пароль"}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=_(""),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder": "Повторите пароль"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )


    def __init__(self, *args, **kwargs):
        super(CreateUser, self).__init__(*args, **kwargs)

        for fieldname in ['email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = get_user_model()
        fields = ('email',)


class LoginForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password
            )

            if self.user_cache is None:
                  raise self.get_invalid_login_error()

            if not self.user_cache.email_verify:
                send_email_for_verify(self.request, self.user_cache)
                raise ValidationError(
                    self.error_messages["unconfirmed_email"],
                    code="unconfirmed_email"
                )

            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    username = forms.CharField(
        widget=forms.EmailInput(attrs={"placeholder": "Введите Email"})
    )

    password = forms.CharField(
        label=_(""),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "placeholder": "Введите пароль"}),
    )

    error_messages = {
        "invalid_login": _(
            "Неправильный Email или пароль"
        ),
        "unconfirmed_email": _(
            "Ваша электронная почта не подтверждена! Мы выслали вам письмо с подтверждением, проверьте свою почту."
        ),
        "inactive": _("Эта учетная запись неактивна"),
    }

