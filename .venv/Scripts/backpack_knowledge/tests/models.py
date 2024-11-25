from django.db import models
from subjects.models import Topic
from django.contrib.auth import get_user_model

from django.conf import settings  # Це дозволяє використовувати CustomUser

CustomUser = get_user_model()

class Test(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='tests')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Тест для {self.topic.title}"

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions', null=True, default=1)  # Зв'язок з тестом
    text = models.TextField()

    def __str__(self):
        return self.text
        
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')  # Зв'язок з питанням
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)  # Поле для визначення правильної відповіді

    def __str__(self):
        return self.text



class TestResult(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Зв'язок з учнем (CustomUser)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    score = models.PositiveIntegerField()  # Кількість правильних відповідей
    total_questions = models.PositiveIntegerField()  # Загальна кількість питань
    percentage = models.FloatField()  # Відсоток правильних відповідей
    submitted_at = models.DateTimeField(auto_now_add=True)  # Час подачі результату

    def __str__(self):
        return f"Результат {self.student.username} для тесту {self.test.title}"
