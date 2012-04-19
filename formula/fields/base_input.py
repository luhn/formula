from field import Field

class Input(Field):
    def __html__(self):
        """Render the <input> tag."""
        r = ['<input type="', self.type, '"']
        if self.placeholder:
            r.extend([' placeholder="', self.placeholder, '"'])
        r.append(' />')
        return ''.join(r)


