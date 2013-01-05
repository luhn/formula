from field import Field

class CheckboxGroup(Field):
    """Class to hold a group of checkboxes."""
    def __init__(self, name, options, escape=True, **kwargs):
        self.options = options
        self._escape = escape
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
            r.append('<label class="checkbox" for="')
            if self.parent_name:
                r.extend([self.parent_name, '_'])
            r.extend([self.name, '_', str(option), '" id="'])
            if self.parent_name:
                r.extend([self.parent_name, '_'])
            r.extend([self.name, '_', str(option), '_label',
                '"><input type="checkbox" name="', self.name, '" id="'])
            if self.parent_name:
                r.extend([self.parent_name, '_'])
            r.extend([self.name, '_', str(option), '" value="', self.escape(option), '"'])
            if self.value and (str(option) in self.value):
                r.append(' checked="checked"')
            r.append(' /> ')
            #If it's a dictionary, get the text, otherwise use the value
            if isinstance(self.options, dict):
                if self._escape:
                    r.append(self.escape(self.options[option]))
                else:
                    r.append(self.options[option])
            else:
                if self._escape:
                    r.append(self.escape(option))
                else:
                    r.append(option)
            r.append('</label>')

        return self.renderer(self, ''.join(r))

