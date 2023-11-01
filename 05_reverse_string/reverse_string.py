def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    phrase_as_list = list(phrase)
    phrase_as_list.reverse()

    return ''.join(phrase_as_list)
