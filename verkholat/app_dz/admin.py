from django.contrib import admin
from .models.student import Student
from django.contrib.admin import register
# Register your models here.

@register(Student)
class AppAdmin(admin.ModelAdmin):
    pass
