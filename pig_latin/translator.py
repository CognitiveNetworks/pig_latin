"""
PigLatin translator takes string input and returns the pig latin translation for this string

The main method for this is translate(sentence|word)
"""
import re


def translate_word(word):
    # I made this a separate function just so it's easily testable. This would word fine as a lambda
    return word[1:] + word[0] + 'ay'


def fix_capitalization(word):
    if not type(word) == str:
        raise TypeError('This only takes string inputs')
    if word.istitle():
        word = word.lower()
        word = translate_word(word)
        return word.capitalize()
    else:
        return translate_word(word)


def translate(sentence):
    word_list = re.split('(\W+)', sentence)  # splits on non-word characters
    if len(word_list) > 1:
        for pos, word in enumerate(word_list):
            match = re.match('(\w+)', word)  # only matches word characters
            if match:
                # replace the word character
                word_list[pos] = fix_capitalization(word)
        return ''.join(word_list)
    else:
        # single word, just translate the single
        return fix_capitalization(sentence)
