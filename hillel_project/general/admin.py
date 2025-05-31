from django.contrib import admin

from general.models import RequestStatistics
from modeltranslation.admin import TranslationAdmin
from .models import Department, Position, Employee

# Register your models here.
@admin.register(RequestStatistics)
class RequestStatisticsAdmin(admin.ModelAdmin):

    list_display = ('user', 'requests')

@admin.register(Department)
class DepartmentAdmin(TranslationAdmin):
    list_display = ('name', 'parent_department')


@admin.register(Position)
class PositionAdmin(TranslationAdmin):
    list_display = ('title', 'department', 'is_manager', 'monthly_rate')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'position')

