from django.db import models
from .course import Course

"""
Детальні профілі студентів:
Додайте наступні поля:
Назва курсу
Фотографія 
phone_number: Номер телефону.
"""

class Student(models.Model):
    class Meta:
        db_table = "it_student_db"

    first_name = models.TextField(null=False)
    last_name = models.TextField(null=False)
    phone_number = models.CharField(null=False)
    completed_lessons = models.IntegerField()
    birth_date = models.DateField(null=True)
    avatar = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

