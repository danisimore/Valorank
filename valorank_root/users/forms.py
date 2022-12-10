from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django import forms


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
        "inactive": _("Эта учетная запись неактивна"),
    }

