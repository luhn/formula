import unittest
from formula import Text
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

    def test_input_with_attributes(self):
        tag = Text('email', classes=['error', 'large'],
                style='font-weight:bold;')
        soup = BeautifulSoup(tag.render())
        self.assertEqual(soup.input['class'], ['error', 'large'])
        self.assertEqual(soup.input['style'], 'font-weight:bold;')

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

    def test_label(self):
        tag = Text('email', label='Email')
        soup = BeautifulSoup(tag.label.render())
        self.assertEqual(soup.label['for'], tag.id)
        self.assertEqual(soup.label.get_text(), 'Email')

    def test_with_wrapper(self):
        tag = Text('email', label='Email')
        soup = BeautifulSoup(tag.wrapper.render())
        self.assertEqual(soup.label.get_text(), 'Email ')
        self.assertEqual(soup.label.input['name'], 'email')

    def test_with_wrapper_align_right(self):
        tag = Text('email', label='Email')
        soup = BeautifulSoup(tag.right_wrapper.render())
        self.assertEqual(soup.label.get_text(), ' Email')
        self.assertEqual(soup.label.input['name'], 'email')

    def test_with_no_label(self):
        tag = Text('email')
        with self.assertRaises(ValueError):
            tag.label.render()
        with self.assertRaises(ValueError):
            tag.wrapper.render()

