"""
PigLatin translator takes string input and returns the pig latin translation for this string

The main method for this is translate(sentence|word)
"""
import re


def translate_word(word):
    """
    This translates a single word into pig latin

    :param word: a single string (no spaces, no capitalization)
    :return: string that is the pig latin translation of a single word
    """
    return word[1:] + word[0] + 'ay'


def fix_capitalization(word):
    """
    This deals with proper capitalization of pig latin words so you don't get a capital letter in the middle of a word

    Calls translate_word after dealing with capital letters, then re-places capitalization with sentence case
    :param word: A single word string
    :return: the translated single word string with sentence case if it had it originally
    """
    if not type(word) == str:
        raise TypeError('This only takes string inputs')
    if word.istitle():
        word = word.lower()
        word = translate_word(word)
        return word.capitalize()
    else:
        return translate_word(word)


def translate(sentence):
    """
    This is the main method, will translate a sentence or single word and deal properly with case, punctuation

    :param sentence: This is a string of any length and capitalization
    :return: The sentence(s) string with capitalization and punctuation in the right place
    """
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
