from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва предмета")
    description = models.TextField(verbose_name="Опис предмета")
    is_for_students = models.BooleanField(default=False, verbose_name="Доступний для учнів")
    students = models.ManyToManyField(
        CustomUser, related_name='subjects', blank=True, verbose_name="Учні"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предмети"
        ordering = ['name']  # Сортування за назвою





class Topic(models.Model):
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='topics', verbose_name="Предмет"
    )
    title = models.CharField(max_length=255, verbose_name="Назва теми")
    description = models.TextField(verbose_name="Опис теми")
    attached_file = models.FileField(
        upload_to='topic_files/%Y/%m/%d/', blank=True, null=True, verbose_name="Прикріплений файл"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Теми"
        ordering = ['title']  # Сортування за назвою