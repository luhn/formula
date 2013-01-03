from field import Field

class RadioGroup(Field):
    """Class for a select field."""
    def __init__(self, name, options, **kwargs):
        self.options = options
        Field.__init__(self, name, **kwargs)

    def __html__(self):
        r = []

        for option in self.options:
            r.append('<label class="radio" id="')
            if self.parent_name:
                r.extend([self.parent_name, '_'])
            r.extend([self.name, '_', str(option), '_label"><input type="radio" name="',
                self.name, '" id="'])
            if self.parent_name:
                r.extend([self.parent_name, '_'])
            r.extend([self.name, '" value="', self.escape(option), '"'])
            if str(option)==self.value:
                r.append(' checked="checked"')
            r.append(' /> ')
            #If it's a dictionary, get the text, otherwise use the value
            if isinstance(self.options, dict):
                r.append(self.escape(self.options[option]))
            else:
                r.append(self.escape(option))
            r.append('</label>')

        return self.renderer(self, ''.join(r))

