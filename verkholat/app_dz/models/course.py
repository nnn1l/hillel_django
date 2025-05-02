from django.db import models

"""
Додайте до моделі Course поле:
Назва курсу
learning_plan: Короткий опис тем
"""

class Course(models.Model):
    name = models.CharField(max_length=75, null=False)
    learning_plan = models.CharField()