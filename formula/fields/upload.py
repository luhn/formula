from field import Field

class Upload(Field):
    """A file upload field."""
    def __html__(self):
        r = ['<input type="file" name="', self.name, '" id="']
        if self.parent_name:
            r.extend([self.parent_name, '_'])
        r.extend([self.name, '"'])
        r.append(' />')
        return self.renderer(self, ''.join(r))

