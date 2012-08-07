from field import Field

class Input(Field):

    def __init__(self, name, **kwargs):
        if 'size' in kwargs:
            self.size = kwargs['size']
            del kwargs['size']
        else:
            self.size = None
        Field.__init__(self, name, **kwargs)

    def __html__(self):
        """Render the <input> tag."""
        r = ['<input type="', self.type, '" name="', self.name, '" id="']
        if self.parent_name:
            r.extend([self.parent_name, '_'])
        r.extend([self.name, '"'])
        if self.classes:
            r.extend([' class="', self.classes, '"'])
        if self.size:
            r.extend([' size="', str(self.size), '"'])
        if self.placeholder:
            r.extend([' placeholder="', self.escape(self.placeholder), '"'])
        if self.value:
            r.extend([' value="', self.escape(self.value), '"'])
        r.append(' />')
        return self.renderer(self, ''.join(r))


