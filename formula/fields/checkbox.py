from field import Field

class Checkbox(Field):
    """A checkbox field."""
    def __init__(self, name, selected_value=1, checked=False, **kwargs):
        self.selected_value = str(selected_value)
        self.checked = checked
        Field.__init__(self, name, **kwargs)

    def __html__(self):
        r = ['<input type="checkbox" name="', self.name, '" id="', self.id(),
                '" value="', self.selected_value, '"']
        if str(self.selected_value)==str(self.value) or self.checked:
            r.append(' checked="checked"')
        r.append(' />')
        return self.renderer(self, ''.join(r))
