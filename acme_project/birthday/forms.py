from django import forms
from django.core.exceptions import ValidationError

from .models import Birthday, Congratulation
from .validators import real_age

BEATLES = {
    'Джон Леннон',
    'Пол Маккартни',
    'Джордж Харрисон',
    'Ринго Старр',
}


# class BirthdayForm(forms.ModelForm):

#     class Meta:
#         model = Birthday
#         fields = (
#             'first_name',
#             'last_name',
#             'birthday',
#             'image',
#             'tags',
#         )
#         widgets = {
#             'birthday': forms.DateInput(
#                 format='%Y-%m-%d',
#                 attrs={'type': 'date'},
#             ),
#         }

#     def clean_first_name(self):
#         first_name = self.cleaned_data['first_name']
#         return first_name.split()[0]

#     def clean(self):
#         cleaned_data = super().clean()
#         first_name = cleaned_data.get('first_name')
#         last_name = cleaned_data.get('last_name')

#         if (
#             first_name
#             and last_name
#             and f'{first_name} {last_name}' in BEATLES
#         ):
#             raise ValidationError(
#                 'Мы тоже любим Битлз, но введите, пожалуйста, '
#                 'настоящее имя!',
#             )

#         return cleaned_data


# class BirthdayForm(forms.Form):
    # first_name = forms.CharField(label='Имя', max_length=20)
    # last_name = forms.CharField(
    #     label='Фамилия', required=False, help_text='Необязательное поле'
    # )
    # birthday = forms.DateField(
    #     label='Дата рождения',
    #     widget=forms.DateInput(attrs={'type': 'date'}),
    #     # В аргументе validators указываем список или кортеж 
    #     # валидаторов этого поля (валидаторов может быть несколько)
    #     validators=(real_age,),
    # )

    # def clean_first_name(self):
    #     # Получаем значение имени из словаря очищенных данных
    #     first_name = self.cleaned_data['first_name']
    #     # Разбиваем полученную строку по пробелам 
    #     # и возвращаем только первое имя
    #     return first_name.split()[0] 

class BirthdayForm(forms.ModelForm):

    class Meta:
        model = Birthday
        fields = (
            "first_name",
            "last_name",
            "birthday",
            "image",
        )
        widgets = {
            "birthday": forms.DateInput(
                format="%Y-%m-%d",
                attrs={"type": "date"},
            ),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if (
            first_name
            and last_name
            and f'{first_name} {last_name}' in BEATLES
        ):
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, '
                'настоящее имя!',
            )

        return cleaned_data 

class CongratulationForm(forms.ModelForm):

    class Meta:
        model = Congratulation
        fields = ('text',)
