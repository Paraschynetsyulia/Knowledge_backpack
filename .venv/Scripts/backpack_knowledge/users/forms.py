# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_type']
        labels = {
            'username': 'Імʼя користувача',
            'email': 'Email адреса',
            'password1': 'Пароль',
            'password2': 'Підтвердження паролю',
            'user_type': 'Тип користувача',
        }
        help_texts = {
            'username': 'Введіть імʼя, яке ви хочете використовувати.',
            'password1': 'Пароль має бути щонайменше 8 символів.',
            'password2': 'Повторно введіть пароль для підтвердження.',
        }
    
    # Поле з вибором типу користувача (переклад на українську)
    user_type = forms.ChoiceField(
        choices=CustomUser.USER_TYPE_CHOICES,
        widget=forms.RadioSelect,
        label='Тип користувача'
    )
