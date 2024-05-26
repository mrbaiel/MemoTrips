from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    vk_id = models.CharField(max_length=35, blank=True, null=True)
    avatar =models.URLField(blank=True, null=True)

class Memory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="memories")
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title