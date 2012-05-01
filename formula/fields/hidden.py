from field import Field

class Hidden(Field):
    """A hidden field."""

    def __html__(self):
        r = ['<input type="hidden" name="', self.name, '" id="', self.id(),
                '"']
        if self.value:
            r.extend([' value="', self.value, '"'])
        r.append(' />')
        return ''.join(r)
