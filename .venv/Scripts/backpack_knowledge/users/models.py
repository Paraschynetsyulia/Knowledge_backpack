from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'вчитель'),
        (2, 'учень'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)  # Додаємо значення за замовчуванням

    # Додаємо related_name до полів groups і user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Додаємо кастомний related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Додаємо кастомний related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
