from django import forms

from .models import Request


class RequestForm(forms.ModelForm):
    """Форма запроса в службу поддержки"""

    class Meta:
        model = Request
        fields = ('email', 'problem_description')
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ваш Email'
                }
            ),
            'problem_description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Опишите вашу проблему'
                }
            )
        }