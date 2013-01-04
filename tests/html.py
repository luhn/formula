import unittest
from bs4 import BeautifulSoup
from formula.html import Tag

class TestHtmlClasses(unittest.TestCase):

    def test_basic_tag(self):
        self.assertEqual(
                Tag('p').render(),
                '<p></p>')

        self.assertEqual(
                Tag('DIV').render(),
                '<div></div>')

        with self.assertRaises(ValueError):
            Tag('div`').render()

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


    def test_init_attributes(self):
        self.assertEqual(
                Tag('img', SRC='http://i.imgur.com/iWHK2.gif').render(),
                '<img src="http://i.imgur.com/iWHK2.gif" />')

        #Now we need to start parsing the HTML, because the attributes are
        #stored in a dict, the order of which is not consistant across all
        #platforms and implementations.
        tag = Tag('img', src='http://i.imgur.com/iWHK2.gif',
                alt='Cats are liquid, not solid.')
        soup = BeautifulSoup(tag.render())

        self.assertEqual(soup.img.name, 'img')
        self.assertEqual(soup.img['src'], 'http://i.imgur.com/iWHK2.gif')
        self.assertEqual(soup.img['alt'], 'Cats are liquid, not solid.')

    def test_set_attribute(self):
        #Now we'll repeat the test, using the set_attribute method.
        tag = Tag('img')
        tag.set_attribute('src', 'http://i.imgur.com/iWHK2.gif')
        tag.set_attribute('alt', 'Cats are liquid, not solid.')
        soup = BeautifulSoup(tag.render())

        self.assertEqual(soup.img.name, 'img')
        self.assertEqual(soup.img['src'], 'http://i.imgur.com/iWHK2.gif')
        self.assertEqual(soup.img['alt'], 'Cats are liquid, not solid.')

    def test_set_attributes(self):
        #And then the set_attributes method
        tag = Tag('img')
        tag.set_attributes({
            'src': 'http://i.imgur.com/iWHK2.gif',
            'alt': 'Cats are liquid, not solid.'
            })
        soup = BeautifulSoup(tag.render())

        self.assertEqual(soup.img.name, 'img')
        self.assertEqual(soup.img['src'], 'http://i.imgur.com/iWHK2.gif')
        self.assertEqual(soup.img['alt'], 'Cats are liquid, not solid.')


    def test_invalid_attributes(self):
        tag = Tag('img')
        with self.assertRaises(ValueError):
            tag.set_attribute('src`', 'http://i.imgur.com/iWHK2.gif')


    def test_escaping_attribute_values(self):
        self.assertEqual(
                Tag('a', href='<">').render(),
                '<a href="<&quot;>"></a>')

    def test_non_string_attributes(self):
        self.assertEqual(
                Tag('p', title=15).render(),
                '<p title="15"></p>')

    def test_set_attribute_shorthand(self):
        tag = Tag('img')
        tag['src'] = 'http://i.imgur.com/iWHK2.gif'
        self.assertEqual(
                tag.render(),
                '<img src="http://i.imgur.com/iWHK2.gif" />')

    def test_get_attribute(self):
        tag = Tag('img', src='http://i.imgur.com/iWHK2.gif',
                alt='Cats are liquid, not solid.')
        self.assertEqual(
                tag.get_attribute('src'),
                'http://i.imgur.com/iWHK2.gif')
        self.assertEqual(
                tag['alt'],
                'Cats are liquid, not solid.')

    def test_invalid_get_attribute(self):
        tag = Tag('img', src='http://i.imgur.com/iWHK2.gif',
                alt='Cats are liquid, not solid.')

        with self.assertRaises(KeyError):
            tag.get_attribute('href')

        with self.assertRaises(KeyError):
            tag['title']


    def test_delete_attribute(self):
        tag = Tag('img', src='http://i.imgur.com/iWHK2.gif',
                alt='Cats are liquid, not solid.')
        tag.delete_attribute('alt')
        self.assertEqual(
                tag.render(),
                '<img src="http://i.imgur.com/iWHK2.gif" />')

        tag = Tag('img', src='http://i.imgur.com/iWHK2.gif',
                alt='Cats are liquid, not solid.')
        del tag['alt']
        self.assertEqual(
                tag.render(),
                '<img src="http://i.imgur.com/iWHK2.gif" />')


