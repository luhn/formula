
import unittest
from bs4 import BeautifulSoup
from formula.rules import Rule, Required
from formula.exceptions import Invalid

class TestRules(unittest.TestCase):

    def test_base_rule(self):
        self.assertRaises(NotImplementedError, Rule)
        self.assertRaises(NotImplementedError, Rule(msg='Foo'), 'bar')

    def test_required(self):
        self.assertRaises(Invalid, Required(), '')
        try:
            Required()('foobar')
        except Invalid:
            self.fail()

