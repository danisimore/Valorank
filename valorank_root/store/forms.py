from django import forms

from .models import Product


class RankSelectionForm(forms.ModelForm):
    """
    Форма для выбора ранга пользователя и ранга, до которого
    он желает забустить свой аккаунт
    """

    class Meta:
        model = Product
        fields = ('base_rank', 'desired_rank')
        widgets = {
            'base_rank': forms.Select(attrs={'class': 'form-select'}),
            'desired_rank': forms.Select(attrs={'class': 'form-select'})
        }

    def __init__(self, *args, **kwargs):
        super(RankSelectionForm, self).__init__(*args, **kwargs)
        self.fields['base_rank'].empty_label = 'Выберите ранг'
        self.fields['base_rank'].label = 'Ваш Ранг'
        self.fields['desired_rank'].empty_label = 'Выберите ранг'
        self.fields['desired_rank'].label = 'Ранг, который вы хотите'