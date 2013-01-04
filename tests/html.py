import unittest
from formula.html import Tag

class TestHtmlClasses(unittest.TestCase):

    def test_basic_tag(self):
        self.assertEqual(
                Tag('p').render(),
                '<p></p>')

        self.assertEqual(
                Tag('DIV').render(),
                '<div></div>')

        #Make sure the HTML alias also works.
        self.assertEqual(
                Tag('span').__html__(),
                '<span></span>')

    def test_self_closing_tag(self):
        self.assertEqual(
                Tag('img').render(),
                '<img />')

        Tag.XHTML = False
        self.assertEqual(
                Tag('img').render(),
                '<img>')

        Tag.XHTML = True #Reset

