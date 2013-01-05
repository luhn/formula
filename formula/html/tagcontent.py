import cgi

class TagContent(object):
    """This class represents the content of an HTML tag.

    :param *args:  The content of the tags as a list of objects.  Valid
        objects either inherit from basestring (notably ``str`` and
        ``unicode``) or have a ``__html__()`` method.

    """


    def __init__(self, *args):
        self.contents = args

    def render(self):
        """Render the content to HTML, escaping the strings and converting any
        objects to HTML."""

        r = []
        for item in self.contents:
            if isinstance(item, basestring):
                r.append(cgi.escape(item, quote=True))
            else:
                r.append(item.__html__())

        return ''.join(r)

    def __html__(self):
        """An alias for render(), for the benefit of templating engines."""
        return self.render()



