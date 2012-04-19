

class Form(object):
    """An object that stores all the fields of the form."""

    fields = {}

    def __init__(self, name):
        self.name = name

    def add(self, field):
        """Add a new field."""
        name = field.name
        field.parent = self
        self.fields[name] = field

    def __getitem__(self, name):
        """Return the field of the corresponding name."""
        return self.fields[name]

    def render_field(self, field):
        """Render a single field."""
        r = ['<p>', field.__html__(), '</p>']
        return ''.join(r)

    def __html__(self):
        """Render all the fields."""
        fields = []
        for name in self.fields:
            field = self.render_field(self.fields[name])
            fields.append(field)
        return ''.join(fields)
