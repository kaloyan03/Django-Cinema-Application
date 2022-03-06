from django.core.exceptions import ValidationError

START_CAPITAL_LETTER_ERROR_MESSAGE = 'Value must start with capital letter'

def validate_start_with_capital_letter(value):
    if value[0].islower():
        raise ValidationError(START_CAPITAL_LETTER_ERROR_MESSAGE)