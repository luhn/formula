from field import Field

class Checkbox(Field):
    """A checkbox field."""
    def __init__(self, name, selected_value=1, **kwargs):
        self.selected_value = str(selected_value)
        Field.__init__(self, name, **kwargs)

    def __html__(self):
        r = ['<input type="checkbox" name="', self.name, '" id="', self.id(),
                '" value="', self.selected_value, '"']
        print str(self.value)
        print str(self.selected_value)
        if str(self.selected_value)==str(self.value):
            r.append(' checked="checked"')
        r.append(' />')
        return self.renderer(self, ''.join(r))
