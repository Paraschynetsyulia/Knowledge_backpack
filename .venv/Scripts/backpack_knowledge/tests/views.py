from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer, Test, Topic 
from subjects.models import Topic

from .forms import QuestionFormSet, AnswerFormSet
from tests.models import Question

from django.http import HttpResponseRedirect

from django.http import JsonResponse
from .models import TestResult



def test_create(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method == 'POST':
        # Створення тесту
        test = Test.objects.create(topic=topic)
        
        # Збереження питань та відповідей
        question_count = len(request.POST.getlist('questions'))
        for i in range(question_count):
            question_text = request.POST.getlist('questions')[i]
            question = Question.objects.create(text=question_text, test=test)

            for j in range(3):  # 3 варіанти відповідей для кожного питання
                answer_text = request.POST.get(f'answers_{i}_{j}')
                if answer_text:
                    is_correct = str(j + 1) == request.POST.get(f'correct_answer_{i}')
                    Answer.objects.create(question=question, text=answer_text, is_correct=is_correct)

        return redirect('topic_detail', topic_id=topic.id)

    return render(request, 'tests/test_create.html', {'topic': topic})
    


def test_detail(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    
    # Отримуємо всі питання, пов'язані з тестом
    questions = test.questions.all()
    
    return render(request, 'tests/test_detail.html', {
        'test': test,
        'questions': questions
    })
    
    
#@login_required
def pass_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions.all()
    score = 0
    total_questions = questions.count()
    results = []

    if request.method == "POST":
        for question in questions:
            question_id = str(question.id)
            selected_answer_id = request.POST.get(f"question_{question_id}")
            if selected_answer_id:
                selected_answer = get_object_or_404(Answer, id=selected_answer_id)
                is_correct = selected_answer.is_correct
                if is_correct:
                    score += 1

                # Додати в результати для відображення
                results.append({
                    "question": question.text,
                    "selected": selected_answer.text,
                    "correct": is_correct
                })

        # Розрахувати відсоток успіху
        percentage = (score / total_questions) * 100

        # Зберегти результат тесту в БД
        test_result = TestResult(
            student=request.user,  # Використовуємо поточного учня (якщо учень авторизований)
            test=test,
            score=score,
            total_questions=total_questions,
            percentage=percentage
        )
        test_result.save()

        # Передати результати у шаблон
        return render(request, "tests/test_result.html", {
            "test": test,
            "score": score,
            "total_questions": total_questions,
            "percentage": percentage,
            "results": results
        })

    return render(request, "tests/test_pass.html", {"test": test, "questions": questions})
    
    

def topic_results(request, topic_id):
    # Отримуємо тему за її id
    topic = Topic.objects.get(id=topic_id)
    
    # Отримуємо результати проходження тестів для цієї теми
    results = TestResult.objects.filter(test__topic=topic)
    
    return render(request, 'subjects/topic_results.html', {
        'topic': topic,
        'results': results
    })


'''
def pass_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions.all()
    score = 0
    total_questions = questions.count()
    results = []

    if request.method == "POST":
        for question in questions:
            question_id = str(question.id)
            selected_answer_id = request.POST.get(f"question_{question_id}")
            if selected_answer_id:
                selected_answer = get_object_or_404(Answer, id=selected_answer_id)
                is_correct = selected_answer.is_correct
                if is_correct:
                    score += 1

                # Додати в результати для відображення
                results.append({
                    "question": question.text,
                    "selected": selected_answer.text,
                    "correct": is_correct
                })

        # Розрахувати відсоток успіху
        percentage = (score / total_questions) * 100

        # Передати результати у шаблон
        return render(request, "tests/test_result.html", {
            "test": test,
            "score": score,
            "total_questions": total_questions,
            "percentage": percentage,
            "results": results
        })

    return render(request, "tests/test_pass.html", {"test": test, "questions": questions})
'''

