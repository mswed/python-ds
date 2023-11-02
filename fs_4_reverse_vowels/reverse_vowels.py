VOWELS = 'aeiouAEIOU'

def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    sl = list(s)
    found_vowels = []
    found_positions = []

    for i, char in enumerate(s):
        if char in VOWELS:
            found_vowels.append(char)
            found_positions.append(i)
    found_positions.reverse()
    for p, idx in zip(found_vowels, found_positions):
        sl[idx] = p

    return ''.join(sl)

