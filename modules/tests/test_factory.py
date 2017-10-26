import unittest
from modules import TokenFactory as Factory


class TestTokenFactory(unittest.TestCase):

    def test_creation_s1vss2(self):
        self.assertEqual(Factory.create_token('S1VsS2').__class__.__name__, 'S1VsS2')

    def test_creation_vthes(self):
        self.assertEqual(Factory.create_token('VTheS').__class__.__name__, 'VTheS')

    def test_creation_edition(self):
        self.assertEqual(Factory.create_token('Edition').__class__.__name__, 'Edition')

    def test_creation_numeral(self):
        self.assertEqual(Factory.create_token('Numeral').__class__.__name__, 'Numeral')

    def test_creation_compound(self):
        self.assertEqual(Factory.create_token('CompoundWord').__class__.__name__, 'CompoundWord')

    def test_creation_random(self):
        self.assertEqual(Factory.create_token('RandomWord').__class__.__name__, 'RandomWord')

    def test_creation_subtitle(self):
        self.assertEqual(Factory.create_token('Subtitle').__class__.__name__, 'Subtitle')

    def test_creation_nonexisting(self):
        # check that s.split fails when the separator is not a string
        with self.assertRaises(ValueError):
            Factory.create_token('NonExistingType')