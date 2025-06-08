from django.test import TestCase
import unittest

from suppliers.laskin import plus, plus_complicated

class LaskinTests(TestCase):
    def test_plus(self):
        # testaa että numerot lasketaan yhteen
        self.assertEqual(plus(7, 2), 9)
        self.assertEqual(plus(7.1, 2.7), 9.8)
    
    def test_plus_complicated(self):
        #testing adding with conditional if clause
        self.assertEqual(plus_complicated(7, 2), 9)
        self.assertEqual(plus_complicated(2, 8), 8)

    @unittest.expectedFailure           #You use @expectedFailure to track known problems without breaking the whole test suite
    def test_plus_should_fail(self):
        self.assertEqual(plus('7', 2), 9)

    # TDD - Test Driven Development
    # The test method must start with test_	✅ test_addition(). Methods not starting with test_ are ignored