from django.urls import path
from . import views
from tests.views import test_create  # Імпорт функції для створення тесту з додатку 'tests'
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.subject_list, name='subjects_list'),  # Список предметів для вчителів
    path('<int:subject_id>/', views.topic_list, name='topic_list'),  # Список тем для конкретного предмета
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),  # Деталі конкретної теми
    path('add/<int:subject_id>/', views.topic_create, name='topic_create'),  # Створення нової теми для конкретного предмета
    path('create/<int:topic_id>/', test_create, name='test_create'),  # Створення тесту для конкретної теми
    path('student_subjects/', views.student_subjects_list, name='student_subjects_list'),  # Список предметів для учнів
	path('student_subjects/<int:subject_id>/', views.topic_list_student, name='topic_list_student'),
	path('topic/student/<int:topic_id>/', views.topic_detail_student, name='topic_detail_student'),
    
    path('subjects/<int:subject_id>/', views.topic_list, name='topic_list'),
    path('subjects/', views.subject_list, name='subject_list'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]