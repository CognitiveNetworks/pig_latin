__author__ = 'markfox'
import unittest
from pig_latin.translator import translate_word, translate, fix_capitalization


class TestPigLatin(unittest.TestCase):

    def test_translate_word_translates(self):
        self.assertEqual(translate_word('world'), 'orldway')

    def test_translate_word_raises_TypeError_integer(self):
        with self.assertRaises(TypeError):
            translate_word(1)

    def test_translate_word_raises_TypeError_dict(self):
        with self.assertRaises(TypeError):
            translate_word({'Test': 'Test Value'})

    def test_fix_capitalization_sentenceCase(self):
        self.assertEqual(fix_capitalization('Hello'), 'Ellohay')

    def test_fix_capitalization_lowerCase(self):
        self.assertEqual(fix_capitalization('hello'), 'ellohay')

    def test_fix_capitalization_upperCase(self):
        self.assertEqual(fix_capitalization('HELLO'), 'ELLOHAY')

    def test_fix_capitalization_raises_TypeError_integer(self):
        with self.assertRaises(TypeError):
            fix_capitalization(1)

    def test_fix_capitalization_raises_TypeError_dict(self):
        with self.assertRaises(TypeError):
            fix_capitalization({'Test': 'Test Value'})

    def test_translate_single_word(self):
        self.assertEqual(translate('hi'), 'ihay')

    def test_translate_two_words(self):
        self.assertEqual(translate('hey you'), 'eyhay ouyay')

    def test_translate_simple_sentence(self):
        self.assertEqual(translate('How are you doing'), 'Owhay reaay ouyay oingday')

    def test_translate_punctuation(self):
        self.assertEqual(translate("I'm doing great! THANKS!"), "Iay'may oingday reatgay! HANKSTAY!")
