from accounts.models import User
from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(auto_now=False, auto_now_add=False)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tasks")
    shared_with = models.ManyToManyField(User, related_name="shared_tasks")
