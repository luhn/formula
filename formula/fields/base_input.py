from field import Field

class Input(Field):
    def __html__(self):
        """Render the <input> tag."""
        r = ['<input type="', self.type, '"']
        if self.placeholder:
            r.extend([' placeholder="', self.escape(self.placeholder), '"'])
        if self.value:
            r.extend([' value="', self.escape(self.value), '"'])
        r.append(' />')
        return ''.join(r)


