from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Реєстрація нового користувача
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Реєстрація успішна!')

            # Вхід після реєстрації
            login(request, user)

            # Перевіряємо, чи це адміністратор (staff)
            if user.is_staff:
                return redirect('/admin/')  # Перенаправляємо до адмінпанелі
            elif user.user_type == 2:  # Якщо студент
                return redirect('student_subjects_list')  # Перелік предметів для студента
            else:  # Якщо вчитель
                return redirect('subjects_list')  # Перелік предметів для вчителя
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})


# Функція для входу користувача
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Ласкаво просимо, {username}!')

                # Перевіряємо, чи це адміністратор (staff)
                if user.is_staff:
                    return redirect('/admin/')  # Перенаправляємо до адмінпанелі
                elif user.user_type == 2:  # Якщо студент
                    return redirect('student_subjects_list')  # Перелік предметів для студента
                else:  # Якщо вчитель
                    return redirect('subjects_list')  # Перелік предметів для вчителя
            else:
                messages.error(request, 'Невірне ім\'я користувача або пароль.')
        else:
            messages.error(request, 'Будь ласка, виправте помилки у формі входу.')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


# Список предметів для вчителя
@login_required
def subjects_list(request):
    subjects = Subject.objects.all()  # Отримуємо всі предмети
    return render(request, 'subjects/subjects_list.html', {'subjects': subjects})

# Список предметів для студента
@login_required
def student_subjects_list(request):
    subjects = Subject.objects.filter(is_for_students=True)  # Фільтруємо предмети для студентів
    return render(request, 'subjects/student_subjects_list.html', {'subjects': subjects})
