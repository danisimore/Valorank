from django.contrib.auth import get_user_model, password_validation, authenticate
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordResetForm as DjangoPasswordResetForm,
    SetPasswordForm as DjangoSetPasswordForm
)
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms

from users.utils import send_email_for_verify


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''                                               Login/Register Forms                                               '''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class CreateUser(UserCreationForm):
    """
    Форма создания пользователя. Используется в представлении SignUpView.
    Наследуется от базового класса Django.
    Переопределены поля, для их отображения в необходимом виде; Значение help_texts
    установленно в None. В классе мета указана модель пользователя, т.к.
    пользователь был переопределен.
    """

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
    """
    Форма авторизации пользователя. Используется в представлении SignInView.
    Унаследована от базового класса авторизации Django. Переопределены поля,
    сообщения об ошибках, а также метод clean.
    Метод clean переопределен для дополнительной проверки подтверждения почты.
    Если почта не подтверждена, то поднимается ValidationError с сообщением
    "unconfirmed_email", и пользователю отправляется письмо с подтверждением.
    Авторизоваться не получится, пока почта не подтверждена.
    """

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
                send_email_for_verify(
                    self.request,
                    self.user_cache,
                    'authentication/verify_email.html',
                    self.user_cache.email
                )
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


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''                                               Password Reset Forms                                               '''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class PasswordResetForm(DjangoPasswordResetForm):
    """Форма сброса пароля. Унаследована от базовой формы сброса пароля Django. Переопределено поле email"""
    email = forms.EmailField(
        label=_(""),
        max_length=254,
        widget=forms.EmailInput(attrs={"placeholder": "Ваш Email"}),
    )


class SetPasswordForm(DjangoSetPasswordForm):
    """
    Форма ввода нового пароля после сброса. Унаследована от базовой формы установки пароля Django.
    Переопределены поля: new_password1, new_password2
    """

    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder": "Введите новый пароль"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder": "Повторите пароль"}),
    )


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''                                                Email Change Forms                                                '''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class EmailChangeForm(forms.Form):
    """Форма для ввода своей почты при смене."""
    email = forms.EmailField(
        label=_(""),
        max_length=254,
        widget=forms.EmailInput(attrs={"placeholder": "Ваш Email"}),
    )

class TemporaryEmailForm(forms.Form):
    """Форма для ввода новой почты при смене."""
    temporary_email = forms.EmailField(
        label=_(""),
        max_length=254,
        widget=forms.EmailInput(attrs={"placeholder": "Ваш Email"}),
    )

    class Meta:
        model = get_user_model()
        fields = ('temporary_email',)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''                                                Password Change Form                                              '''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class PasswordChangeForm(SetPasswordForm):
    """
    Форма для смены пароля. Унаследовано от базового класса установки пароля Django.
    Добавлено поле old_password.
    """

    new_password1 = forms.CharField(
        label=_(""),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder": "Введите новый пароль"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_(""),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder": "Повторите новый пароль"}),
    )

    error_messages = {
        **SetPasswordForm.error_messages,
        "password_incorrect": _(
            "Your old password was entered incorrectly. Please enter it again."
        ),
        "password_mismatch": _("The two password fields didn’t match."),
    }
    old_password = forms.CharField(
        label=_(""),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True, "placeholder": "Введите свой текущий пароль"}
        ),
    )

    field_order = ["old_password", "new_password1", "new_password2"]

    def clean_old_password(self):
        """
        Validate that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise ValidationError(
                self.error_messages["password_incorrect"],
                code="password_incorrect",
            )
        return old_password