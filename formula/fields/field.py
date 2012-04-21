from formula.exceptions import Invalid

class Field(object):

    def __init__(self, name, label=None, placeholder=None, value=None,
            renderer=None):
        self.name = name
        self.label = label
        self.placeholder = placeholder
        self.value = value
        self.renderer = renderer
        self._rules = []
        self._filters = []
        self.errors = []
        self.parent_name = None

    def rules(self, *args):
        """Set some validators."""
        self._rules.extend(args)
        return self

    def filters(self, *args):
        """Similar to rules, except filters are always run first."""
        self._filters.extend(args)
        return self

    def validate(self, value):
        """Run the value through all the validators."""
        self.value = value

        for f in self._filters:
            self.value = f(self.value)

        erred = False
        for rule in self._rules:
            try:
                new = rule(self.value)
                if new:
                    self.value = new
            except Invalid as e:
                erred = True
                self.errors.append(str(e))
        if erred:
            raise Invalid()

    html_escape_table = {
        "&": "&amp;",
        '"': "&quot;",
        "'": "&apos;",
        ">": "&gt;",
        "<": "&lt;",
        }

    def escape(self, text):
        """A very, very basic way of escaping HTML entities, taken from
        http://wiki.python.org/moin/EscapingHtml"""
        return "".join(self.html_escape_table.get(c,c) for c in text)
