import re

void_elements = {'area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img',
        'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

class Tag(object):
    """A Tag object represents an HTML tag, and will be rendered into HTML."""

    #: Enables XML-style HTML.
    XHTML = True

    #: The regex checked against the tag name and attributes.
    valid_attr_regex = re.compile('[a-zA-Z_:][-a-zA-Z0-9_:.]*$')

    def __init__(self, tag_name, **kwargs):
        """Construct an object representing an HTML tag.

        :param tag_name: The HTML tag name.  Must match valid_attr_regex.
        :type tag_name: str
        :param **kwargs:  All the additional keyword arguments will be set
            as attributes.

        """

        if not re.match(self.valid_attr_regex, tag_name):
            raise ValueError('Invalid tag name.')

        self.tag_name = tag_name.lower()
        self.self_closing = tag_name in void_elements
        self.attributes = {}

        #Set all the attributes passed in.
        for (key, value) in kwargs.iteritems():
            self.set_attribute(key, value)

    def set_attribute(self, name, value):
        """Set a single attribute to value.

        :param name:  The attribute name.  Must match valid_attr_regex.
        :type name:  str
        :param value:  The value for the attribute.  Double quotes will
            automatically be escaped.
        :type value:  str

        """

        if not re.match(self.valid_attr_regex, name):
            raise ValueError('"' + name +'" is an invalid attribute name.')

        self.attributes[name.lower()] = value


    def set_attributes(self, attributes):
        """Set multiple attributes.

        :param attributes:  A dictionary of the attributes.
        :type attributes:  dict

        """

        for name, value in attributes.iteritems():
            self.set_attribute(name, value)


    def render(self):
        """Render the object into a string of HTML."""
        r = ['<', self.tag_name ]

        #Put in the attributes
        for (name, value) in self.attributes.iteritems():
            r.extend([' ', name, '="', escape_quotes(value), '"'])

        #Close the tag
        if self.self_closing:
            if self.XHTML:
                r.append(' />')
            else:
                r.append('>')
        else:
            r.extend(['></', self.tag_name, '>'])

        #Smoosh it all together and return
        return ''.join(r)


    def __html__(self):
        """An alias of render.  For use with templating engines."""
        return self.render()


def escape_quotes(value):
    return value.replace('"', '&quot;')


