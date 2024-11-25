from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject, Topic
from .forms import TopicForm  # Імпортуйте форму TopicForm
from tests.models import Question, Answer  # Імпортуйте моделі для тесту
from django.contrib.auth.decorators import login_required  # Імпортуйте login_required
from tests.models import Test  # Додайте імпорт моделі Test

from tests.models import TestResult, Test


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/subject_list.html', {'subjects': subjects})
	
def topic_list(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    topics = subject.topics.all()  # Використовуємо related_name 'topics'
    return render(request, 'subjects/topic_list.html', {'subject': subject, 'topics': topics})



def topic_detail(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    test_exists = Test.objects.filter(topic=topic).exists()
    test = Test.objects.filter(topic=topic).first() if test_exists else None
    
    # Отримуємо результати для пройдених тестів цієї теми
    results = TestResult.objects.filter(test__topic=topic, student=request.user)

    return render(request, 'subjects/topic_detail.html', {
        'topic': topic,
        'test_exists': test_exists,
        'test': test,
        'results': results
    })
	
'''
def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    
    # Перевіряємо, чи є тест для цієї теми
    test_exists = Test.objects.filter(topic=topic).exists()
    
    # Отримуємо сам тест (якщо він існує)
    test = Test.objects.filter(topic=topic).first() if test_exists else None
    
    return render(request, 'subjects/topic_detail.html', {
        'topic': topic,
        'test_exists': test_exists,
        'test': test
    })
'''

def topic_create(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)  # Отримуємо предмет за ID

    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)  # Створіть форму, якщо є файли
        if form.is_valid():
            topic = form.save(commit=False)  # Не зберігайте поки
            topic.subject = subject  # Призначте предмет
            topic.save()  # Тепер збережіть тему
            return redirect('topic_list', subject_id=subject.id)  # Перенаправлення на список тем
    else:
        form = TopicForm()

    return render(request, 'subjects/topic_form.html', {'form': form, 'subject': subject})

	
def student_subjects_list(request):
    subjects = Subject.objects.filter(students=request.user)  # Отримуємо предмети для поточного студента
    return render(request, 'subjects/student_subjects.html', {'subjects': subjects})


# Список предметів для вчителя
@login_required
def subjects_list(request):
    subjects = Subject.objects.all()  # Отримуємо всі предмети
    return render(request, 'subjects/subjects_list.html', {'subjects': subjects})

# Список предметів для студента
@login_required
def student_subjects_list(request):
    subjects = Subject.objects.all()  # Фільтруємо предмети для студентів
    return render(request, 'subjects/student_subjects_list.html', {'subjects': subjects})
	
	
def topic_list_student(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    topics = subject.topics.all()  # Використовуємо related_name 'topics'
    return render(request, 'subjects/topic_list_student.html', {'subject': subject, 'topics': topics})
    

def topic_detail_student(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    test_exists = Test.objects.filter(topic=topic).exists()  # Перевірка наявності тесту
    
    test = Test.objects.filter(topic=topic).first() if test_exists else None  # Отримуємо тест, якщо існує

    return render(request, 'subjects/topic_detail_student.html', {
        'topic': topic,
        'test_exists': test_exists,
        'test': test
    })

	
'''    
def topic_detail_student(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    return render(request, 'subjects/topic_detail_student.html', {'topic': topic})
'''


	
	


