import unittest
import rgng


class TestNameGenerator(unittest.TestCase):

    def test_generate_name(self):
        self.assertNotEquals(rgng.generate_name(),'')