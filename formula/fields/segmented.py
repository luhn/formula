from field import Field

class Segmented(Field):
    """A segmented control unique to Twitter Bootstrap."""
    def __init__(self, name, options, **kwargs):
        self.options = options
        Field.__init__(self, name, **kwargs)

    def __html__(self):
        r = ['<div class="btn-toolbar">',
                '<div class="btn-group" id="', self.id(), '">']
        for option in self.options:
            r.extend(['<a href="#" data-value="', self.escape(option),
                '" class="btn'])
            if str(option)==self.value:
                r.append(' active')
            r.append('">')
            #If it's a dictionary, get the text, otherwise use the value
            if isinstance(self.options, dict):
                r.append(self.escape(self.options[option]))
            else:
                r.append(self.escape(option))
            r.append('</a>')

        r.append('</div></div>')
        return self.renderer(self, ''.join(r))
