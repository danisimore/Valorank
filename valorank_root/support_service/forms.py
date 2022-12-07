from django import forms

from .models import Request

class RequestForm(forms.ModelForm):

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