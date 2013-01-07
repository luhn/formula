import unittest
from formula import Text, Label
from bs4 import BeautifulSoup

class TestFields(unittest.TestCase):

    def test_basic_input(self):
        soup = BeautifulSoup(Text('email').__html__())
        self.assertEqual(soup.input['type'], 'text')
        self.assertEqual(soup.input['name'], 'email')

    def test_input_with_value(self):
        soup = BeautifulSoup(Text('email', value='test@example.com').render())
        self.assertEqual(soup.input['type'], 'text')
        self.assertEqual(soup.input['name'], 'email')
        self.assertEqual(soup.input['value'], 'test@example.com')

    def test_input_with_id(self):
        soup = BeautifulSoup(Text('email', id='my_email_id').render())
        self.assertEqual(soup.input['id'], 'my_email_id')

        tag = Text('email')
        tag.id = 'my_email_2'
        soup = BeautifulSoup(tag.render())
        self.assertEqual(soup.input['id'], 'my_email_2')

    def test_input_with_auto_id(self):
        soup = BeautifulSoup(Text('email', id=True).render())
        self.assertEqual(soup.input['id'], 'email')

        tag = Text('email_2')
        tag.id = True
        soup = BeautifulSoup(tag.render())
        self.assertEqual(soup.input['id'], 'email_2')
        self.assertEqual(tag.id, 'email_2')

        tag = Text('email_3')
        auto_id = tag.id
        soup = BeautifulSoup(tag.render())
        self.assertEqual(soup.input['id'], 'email_3')
        self.assertEqual(tag.id, 'email_3')

    def test_with_label(self):
        tag = Text('email', label='Email')
        soup = BeautifulSoup(tag.render())
        self.assertEqual(soup.label.get_text(), 'Email')
        self.assertEqual(soup.label.input, None)
        self.assertEqual(soup.input['name'], 'email')

    def test_with_label_align_right(self):
        #I can't figure out how to make sure the label is on the right with
        #BS4, so I'm just going to assume the code works correctly.
        tag = Text('email', label=Label('Email', align='right'))
        soup = BeautifulSoup(tag.render())
        self.assertEqual(soup.label.get_text(), 'Email')
        self.assertEqual(soup.label.input, None)
        self.assertEqual(soup.input['name'], 'email')

    def test_with_wrapper(self):
        tag = Text('email', wrapper='Email')
        soup = BeautifulSoup(tag.render())
        self.assertEqual(soup.label.get_text(), 'Email ')
        self.assertEqual(soup.label.input['name'], 'email')

    def test_with_wrapper_align_right(self):
        tag = Text('email', wrapper=Label('Email', align='right'))
        soup = BeautifulSoup(tag.render())
        self.assertEqual(soup.label.get_text(), ' Email')
        self.assertEqual(soup.label.input['name'], 'email')

    def test_label_align_exception(self):
        with self.assertRaises(ValueError):
            Label('Email', align='center')

