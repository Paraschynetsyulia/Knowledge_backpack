from django.contrib import admin
from .models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Відображення полів у списку предметів
    search_fields = ('name',)  # Додати поле для пошуку за ім'ям предмета
