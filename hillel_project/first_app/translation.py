from modeltranslation.translator import TranslationOptions, register

from .models import Position, Department

@register(Department)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Position)
class PositionTranslationOption(TranslationOptions):
    fields = ("title", "description")


