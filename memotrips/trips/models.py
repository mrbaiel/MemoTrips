from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    vk_id = models.CharField(max_length=35, blank=True, null=True)
    avatar =models.URLField(blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Добавлено для разрешения конфликта
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Добавлено для разрешения конфликта
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="memories")
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title