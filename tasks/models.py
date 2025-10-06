from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)   # Task title
    done = models.BooleanField(default=False)  # Whether task is completed
    created_at = models.DateTimeField(auto_now_add=True)  # When task was created

    def __str__(self):
        return self.title