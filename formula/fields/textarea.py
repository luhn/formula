from field import Field

class Textarea(Field):
    """Class for a textarea field"""

    def __init__(self, name, cols=25, rows=3, **kwargs):
        self.cols = cols
        self.rows = rows
        Field.__init__(self, name, **kwargs)

    def __html__(self):
        """Render the <input> tag."""
        r = ['<textarea name="', self.name, '" id="']
        if self.parent_name:
            r.extend([self.parent_name, '_'])
        r.extend([self.name, '" rows="', str(self.rows), '" cols="',
            str(self.cols), '">'])
        if self.value:
            r.append(self.escape(unicode(self.value)))
        r.append('</textarea>')
        return self.renderer(self, ''.join(r))
