from django.core.exceptions import ValidationError
from cinema_app.validators import validate_start_with_capital_letter

WORD_START_WITH_CAPITAL_LETTER_ERROR_MESSAGE = 'Every word must start with capital letter'


# def validate_word_start_with_capital_letter(value):
#     is_valid = True
#     words = value.split(' ')
#     if len(words) == 1:
#         if words[0][0].islower():
#             is_valid = False
#
#     else:
#         is_valid = all([word[0].isupper() for word in words])
#
#     if not is_valid:
#         raise ValidationError(WORD_START_WITH_CAPITAL_LETTER_ERROR_MESSAGE)

def validate_word_start_with_capital_letter(value):
    words = value.split(' ')

    try:
        for word in words:
            validate_start_with_capital_letter(word)

    except ValidationError:
        raise ValidationError(WORD_START_WITH_CAPITAL_LETTER_ERROR_MESSAGE)


