from field import Field

class CheckboxGroup(Field):
    """Class to hold a group of checkboxes."""
    def __init__(self, name, options, **kwargs):
        self.options = options
        Field.__init__(self, name, **kwargs)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value is None:
            self._value = []
        elif isinstance(value, list):
            self._value = map(lambda x: str(x), value)
        else:
            self._value = [str(value)]

    def __html__(self):
        r = []

        for option in self.options:
            r.extend(['<label class="checkbox">',
                '<input type="checkbox" name="', self.name, '" id="'])
            if self.parent_name:
                r.extend([self.parent_name, '_'])
            r.extend([self.name, '" value="', self.escape(option), '"'])
            if self.value and (str(option) in self.value):
                r.append(' checked="checked"')
            r.append(' /> ')
            #If it's a dictionary, get the text, otherwise use the value
            if isinstance(self.options, dict):
                r.append(self.escape(self.options[option]))
            else:
                r.append(self.escape(option))
            r.append('</label>')

        return self.renderer(self, ''.join(r))

