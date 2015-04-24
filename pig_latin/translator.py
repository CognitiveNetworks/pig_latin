"""
PigLatin translator takes string input and returns the pig latin translation

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
    This deals with proper capitalization of pig latin words

    Calls translate_word after dealing with capital letters, then replaces
    capitalization with sentence case
    :param word: A single word string
    :return: the translated single word string with sentence case if it had it originally
    """
    if not type(word) == str:
        raise TypeError('This only takes string inputs')
    if word.istitle():
        word = word.lower()
        return translate_word(word).capitalize()
    if word.isupper():
        return translate_word(word).upper()
    else:
        return translate_word(word)


def translate(sentence):
    """
    This will translate a sentence or single word into pig latin

    :param sentence: This is a string of any length and capitalization
    :return: The sentence(s) string with capitalization and punctuation in the right place
    """
    # splits on non-word characters
    word_list = re.split('(\W+)', sentence)  #pylint: disable=W1401, I0011
    if len(word_list) > 1:
        for pos, word in enumerate(word_list):
            # only matches word characters
            match = re.match('(\w+)', word)  #pylint: disable=W1401, I0011
            if match:
                # replace the word character
                word_list[pos] = fix_capitalization(word)
        return ''.join(word_list)
    else:
        # single word, just translate the single
        return fix_capitalization(sentence)
