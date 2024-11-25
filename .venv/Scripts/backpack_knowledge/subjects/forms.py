from django import forms
from .models import Topic  # Імпортуйте модель Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description', 'attached_file']  # Поля, які ви хочете включити
        labels = {
            'title': 'Назва',
            'description': 'Опис',
            'attached_file': 'Файл',
        }

        
