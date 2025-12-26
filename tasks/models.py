from django.db import models


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('in_progress', 'В работе'),
        ('completed', 'Завершено'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(default='pending', choices=STATUS_CHOICES)
    priority = models.CharField(default='medium', choices=PRIORITY_CHOICES)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
