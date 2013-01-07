import re

from tagcontent import TagContent

void_elements = {'area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img',
        'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

class Tag(object):
    """
    A Tag object represents an HTML tag, and will be rendered into HTML.

    :param tag_name: The HTML tag name.  Must match valid_attr_regex.
    :type tag_name: str
    :param content:  The content of the tag.
    :param type:  str, list, TagContent, or None
    :param kwargs:  Attributes of the function.

    Because PEP8 suggests that any argument name clashing with a reserved
    keyword should be appended with an underscore, any attribute names with
    trailing underscores will be trimmed.

    A basic use of the class::

        Tag('p', 'Hello world!', class_=['bold', 'italic'],
            style='background:red;')

    When rendered, this will result in::

        <p class="bold italic" style="backround:red;">Hello world!</p>

    :cvar valid_attr_regex: ``[a-zA-Z_:][-a-zA-Z0-9_:\.]*$``
    :cvar valid_id_regex: ``[a-zA-Z][a-zA-Z0-9-_:\.]*$``
    :cvar valid_class_regex: ``-?[_a-zA-Z]+[_a-zA-Z0-9-]*$``

    """

    #: Enables XML-style HTML.
    XHTML = True

    valid_attr_regex = re.compile(r'[a-zA-Z_:][-a-zA-Z0-9_:\.]*$')

    valid_id_regex = re.compile(r'[a-zA-Z][a-zA-Z0-9-_:\.]*$')

    valid_class_regex = re.compile(r'-?[_a-zA-Z]+[_a-zA-Z0-9-]*$')

    def __init__(self, tag_name, content=None, **kwargs):
        """Initialize blah.


        """

        if not re.match(self.valid_attr_regex, tag_name):
            raise ValueError('Invalid tag name.')

        self.tag_name = tag_name.lower()

        if content is None:
            self.content = None
        elif isinstance(content, list):
            self.content = TagContent(*content)
        elif isinstance(content, TagContent):
            self.content = content
        else:
            self.content = TagContent(content)

        self.self_closing = tag_name in void_elements
        self.attributes = {}
        self._classes = []

        #Set all the attributes passed in.
        for (key, value) in kwargs.iteritems():
            self.set_attribute(key, value)

    @property
    def classes(self):
        """A list of the classes in the classes attribute.  Can be set directly
        or via set_attribute(), and a string will be split up along the
        whitespace.  It's worth noting that, as a list, you should feel free
        to use append() and extend()."""
        return self._classes

    @classes.setter
    def classes(self, value):
        if isinstance(value, str):
            value = value.split()
        for item in value:
            if not self.valid_class_regex.match(item):
                raise ValueError('"' + item + '" is not a valid class name.')
        self._classes = value

    def set_attribute(self, name, value):
        """Set a single attribute to value.

        :param name:  The attribute name.  Must match valid_attr_regex.
        :type name:  str
        :param value:  The value for the attribute.  Double quotes will
            automatically be escaped when rendering.
        :type value:  str

        If you are setting the name or id attribute, the value must conform to
        valid_id_regex.

        """

        if value is None:
            return

        name = name.rstrip('_')

        if not self.valid_attr_regex.match(name):
            raise ValueError('"' + name +'" is an invalid attribute name.')

        if name == 'id' or name == 'name':
            if not self.valid_id_regex.match(value):
                raise ValueError('"' + value +'" is not a valid value for ' +
                        'the name or id attribute.')

        #A special case for the class attribute
        if name == 'class' or name == 'classes':
            self.classes = value
            return

        self.attributes[name.lower()] = str(value)


    def set_attributes(self, attributes):
        """Set multiple attributes.

        :param attributes:  A dictionary of the attributes.
        :type attributes:  dict

        """

        for name, value in attributes.iteritems():
            self.set_attribute(name, value)


    def __setitem__(self, name, value):
        """Set an attribute using item assignment."""
        self.set_attribute(name, value)

    def get_attribute(self, name):
        """Get the value of an attribute."""
        return self.attributes[name]

    def __getitem__(self, name):
        """Get an attribute using self[name]"""
        return self.get_attribute(name)

    def delete_attribute(self, name):
        """Remove an attribute."""
        del self.attributes[name]

    def __delitem__(self, name):
        """Delete an attribute using del self[name]"""
        self.delete_attribute(name)


    def render(self):
        """Render the object into a string of HTML."""
        r = ['<', self.tag_name ]

        #Put in the attributes
        for (name, value) in self.attributes.iteritems():
            r.extend([' ', name, '="', escape_quotes(value), '"'])

        #Put in the classes
        if self.classes:
            r.extend([' class="', ' '.join(self.classes), '"'])

        #Close the tag
        if self.self_closing and not self.content:
            if self.XHTML:
                r.append(' />')
            else:
                r.append('>')
        else:
            r.extend(['>', self.content.render() if self.content else '', '</',
                self.tag_name, '>'])

        #Smoosh it all together and return
        return ''.join(r)


    def __html__(self):
        """An alias of render.  For use with templating engines."""
        return self.render()


def escape_quotes(value):
    return value.replace('"', '&quot;')


