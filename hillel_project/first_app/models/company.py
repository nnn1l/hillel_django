from django.core.exceptions import ValidationError
from django.db import models

"""
Створіть модель під назвою Company, яка міститиме наступні поля:
name: Назва компанії (CharField).
address: Адреса компанії (CharField).
email: Електронна адреса компанії (EmailField).
tax_code: Податковий код компанії (CharField).
Забезпечте, щоб ця модель мала лише один інстанс
Додайте метод __str__
Додайте поле logo до моделі Company, яке дозволятиме завантажувати логотипи компанії
"""

class Company(models.Model):
    name = models.Charfield(max_length=50, null=False)
    adress = models.Charfield()
    email = models.EmailField()
    tax_code = models.Charfield(null=False)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Забезпечення того, що існує лише один інстанс
        if not self.pk and Company.objects.exists():
            raise ValidationError('There can be only one Company instance.')
        return super(Company, self).save(*args, **kwargs)