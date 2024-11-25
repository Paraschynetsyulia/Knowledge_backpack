from django.contrib import admin
from .models import Subject, Topic

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'description')  # Відображення полів у списку тем
    list_filter = ('subject',)  # Фільтрація за предметами
    search_fields = ('title', 'subject__name')  # Додати поле для пошуку
