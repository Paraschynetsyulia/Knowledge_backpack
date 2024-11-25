# tests/forms.py
from django import forms
from .models import Question, Answer

from django import forms
from django.forms import modelformset_factory
from tests.models import Question, Answer

# Форма для питань
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

# Форма для відповідей
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'is_correct']

# Набори форм
QuestionFormSet = modelformset_factory(Question, form=QuestionForm, extra=1, can_delete=True)
AnswerFormSet = modelformset_factory(Answer, form=AnswerForm, extra=3, can_delete=True)