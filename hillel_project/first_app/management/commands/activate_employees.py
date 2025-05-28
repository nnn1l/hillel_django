from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Activates all employees (sets is_active=True).'

    def handle(self, *args, **options):
        User = get_user_model() # Отримуємо модель користувача
        updated_count = User.objects.all().update(is_active=True)

        self.stdout.write(self.style.SUCCESS(
            f'Successfully activated {updated_count} employees.'
        ))