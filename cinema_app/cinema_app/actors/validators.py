from django.core.exceptions import ValidationError

ONLY_LETTERS_ERROR_MESSAGE = 'Value must contain only letters'


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError(ONLY_LETTERS_ERROR_MESSAGE)


