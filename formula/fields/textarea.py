from field import Field

class Textarea(Field):
    """Class for a textarea field"""

    def __init__(self, *args, **kwargs):
        if 'rows' in kwargs:
            self.rows = kwargs['rows']
        else:
            self.rows = 3
        Field.__init__(self, *args, **kwargs)

    def __html__(self):
        """Render the <input> tag."""
        r = ['<textarea name="', self.name, '" id="']
        if self.parent_name:
            r.extend([self.parent_name, '_'])
        r.extend([self.name, '" rows="', str(self.rows), '">'])
        if self.value:
            r.append(self.escape(str(self.value)))
        r.append('</textarea>')
        return self.renderer(self, ''.join(r))
