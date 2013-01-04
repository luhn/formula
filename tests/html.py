import unittest
from bs4 import BeautifulSoup
from formula.html import Tag, TagContent

class TestHtmlClasses(unittest.TestCase):

    ######################
    # Test the Tag class #
    ######################

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

    def test_id_attribute(self):
        self.assertEqual(
                Tag('p', id_='paragraph').render(),
                '<p id="paragraph"></p>')

    def test_invalid_id_attribute(self):
        with self.assertRaises(ValueError):
            Tag('p', id_='#paragraph')

    def test_invalid_name_attribute(self):
        with self.assertRaises(ValueError):
            Tag('p', name='#paragraph')

    def test_classes_as_string(self):
        self.assertEqual(
                Tag('p', class_='paragraph bold').render(),
                '<p class="paragraph bold"></p>')

    def test_classes_as_list(self):
        self.assertEqual(
                Tag('p', class_=['paragraph', 'bold']).render(),
                '<p class="paragraph bold"></p>')

        tag = Tag('p', class_=['paragraph'])
        tag.classes.append('bold')
        self.assertEqual(
                tag.render(),
                '<p class="paragraph bold"></p>')

    def test_classes_as_string_and_list(self):
        tag = Tag('p', class_='paragraph bold')
        tag.classes.append('italic')
        self.assertEqual(
                tag.render(),
                '<p class="paragraph bold italic"></p>')

    def test_invalid_class_name(self):
        with self.assertRaises(ValueError):
            Tag('p', class_='-h`')


    #############################
    # Test the TagContent class #
    #############################

    def test_string_tag_content(self):
        self.assertEqual(
                TagContent('test').render(),
                'test')

        self.assertEqual(
                TagContent('test').__html__(),
                'test')

    def test_multi_string_tag_content(self):
        self.assertEqual(
                TagContent('hello', 'world').render(),
                'helloworld')

    def test_string_tag_content_escape(self):
        self.assertEqual(
                TagContent('<hello>', '&world').render(),
                '&lt;hello&gt;&amp;world')

    def test_html_tag_content(self):

        self.assertEqual(
                TagContent(SomeHtml()).render(),
                '<html>')

    def test_mixed_tag_content(self):
        self.assertEqual(
                TagContent('hello', SomeHtml(), 'world').render(),
                'hello<html>world')



    ####################################
    # Test Tag and TagContent together #
    ####################################

    def test_tag_with_string(self):
        self.assertEqual(
                Tag('p', 'Hello world!').render(),
                '<p>Hello world!</p>')

    def test_tag_with_list(self):
        self.assertEqual(
                Tag('p', [ 'Hello ', Tag('span', 'w'), 'orld.']).render(),
                '<p>Hello <span>w</span>orld.</p>')

    def test_tag_with_tagcontent(self):
        self.assertEqual(
                Tag('p', TagContent('Hello world')).render(),
                '<p>Hello world</p>')

    #And now... For the FINAL TEST!
    def test_boss(self):
        field = Tag('input', type_='text', value='test@example.com',
                placeholder='Required', id_='my_field')
        label = Tag('label', ['Email: ', field], for_='my_field')
        soup = BeautifulSoup(label.render())

        self.assertNotEqual(soup.label, None)
        self.assertNotEqual(soup.label.input, None)
        self.assertEqual(soup.label['for'], 'my_field')
        self.assertEqual(soup.label.get_text(), 'Email: ')




class SomeHtml(object):
    def __html__(self):
        return '<html>'
