from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from ..models import Department, Position

def homework_querysets(request):
    '''Запит 1: Знайдіть усі відділи (Department), у яких є позиції менеджерів, та впорядкуйте їх за назвою відділу в алфавітному порядку.
    Використовуйте filter() і order_by().'''
    departments_with_managers = Department.objects.filter(positions__is_manager=True).order_by('name')
    departments_with_managers_data = list(departments_with_managers.values('name'))

    '''Запит 2: Знайдіть загальну кількість активних позицій (Position).
    Використовуйте filter() та count().'''
    active_positions_count = Position.objects.filter(is_active=True).count()

    '''Запит 3: Виберіть усі позиції, які є активними або які належать до відділу з назвою "HR".
    Використовуйте filter() і OR (|). '''
    active_or_hr_positions = Position.objects.filter(Q(is_active=True) | Q(department__name="HR"))
    active_or_hr_positions_data = list(active_or_hr_positions.values('title', 'is_active', 'department__name'))

    '''Запит 4: Виберіть назви всіх відділів (Department), в яких є менеджери.
    Використовуйте filter() та values().'''
    department_names_with_managers = Department.objects.filter(positions__is_manager=True).values('name').distinct()
    department_names_with_managers_data = list(department_names_with_managers)

    '''Запит 5: Виберіть усі позиції, відсортовані за назвою, але виводьте лише назву та інформацію про активність.
    Використовуйте order_by() і values().'''
    positions_title_and_active = Position.objects.order_by('title').values('title', 'is_active')
    positions_title_and_active_data = list(positions_title_and_active)

    response_data = {
        "query_1_departments_with_managers": departments_with_managers_data,
        "query_2_active_positions_count": active_positions_count,
        "query_3_active_or_hr_positions": active_or_hr_positions_data,
        "query_4_department_names_with_managers": department_names_with_managers_data,
        "query_5_positions_title_and_active": positions_title_and_active_data,
    }
    # ensure_ascii=False дозволяє коректно відображати кирилицю в JSON
    # indent=4 робить JSON більш читабельним
    return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False, 'indent': 4})