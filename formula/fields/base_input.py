from field import Field

class Input(Field):
    def __html__(self):
        """Render the <input> tag."""
        r = ['<input type="', self.type, '" name="', self.name, '" id="']
        if self.parent_name:
            r.extend([self.parent_name, '_'])
        r.extend([self.name, '"'])
        if self.placeholder:
            r.extend([' placeholder="', self.escape(self.placeholder), '"'])
        if self.value:
            r.extend([' value="', self.escape(str(self.value)), '"'])
        r.append(' />')
        return self.renderer(self, ''.join(r))


