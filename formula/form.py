

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

    def values(self, values):
        """Set and validate all submitted form data."""
        for key in values:
            self[key].value = values[key]

    def __getitem__(self, name):
        """Return the field of the corresponding name."""
        return self.fields[name]

    def render_field(self, field):
        """Render a single field."""
        if isinstance(field, str):
            field = self[field]
        r = ['<p>', field.__html__(), '</p>']
        return ''.join(r)

    def __call__(self):
        """Render all the fields."""
        fields = []
        for name in self.fields:
            field = self.render_field(self.fields[name])
            fields.append(field)
        return ''.join(fields)

    def __html__(self):
        """For the sake of templating engines."""
        return self()
