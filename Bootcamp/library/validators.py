from django.core.exceptions import ValidationError


# Не пригодился, django в формах сам обрезает пробелы
def validate_spaces(text: str):
    if text.startswith(' ') or text.endswith(' '):
        raise ValidationError('Поле должно быть без пробельных символов в начале и в конце строки.')
