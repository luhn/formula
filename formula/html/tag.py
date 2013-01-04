void_elements = {'area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img',
        'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

class Tag(object):
    """A Tag object represents an HTML tag, and will be rendered into HTML."""

    #: Enables XML-style HTML.
    XHTML = True

    def __init__(self, tag_name):
        """Construct an object representing an HTML tag.

        :param tag_name: The HTML tag name
        :type tag_name: str

        """

        self.tag_name = tag_name.lower()
        self.self_closing = tag_name in void_elements

    def render(self):
        """Render the object into a string of HTML."""
        r = ['<', self.tag_name ]
        if self.self_closing:
            if self.XHTML:
                r.append(' />')
            else:
                r.append('>')
        else:
            r.extend(['></', self.tag_name, '>'])
        return ''.join(r)

    def __html__(self):
        """An alias of render.  For use with templating engines."""
        return self.render()


