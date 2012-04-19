from exceptions import Invalid
from renderers import twitter_bootstrap

class Form(object):
    """An object that stores all the fields of the form."""

    fields = {}

    def __init__(self, name, renderer = None):
        self.name = name
        if renderer == None:
            renderer = twitter_bootstrap
        self.renderer = renderer

    def add(self, field):
        """Add a new field."""
        name = field.name
        if not field.renderer:
            field.renderer = self.renderer
        field.parent_name = self.name
        self.fields[name] = field

    def values(self, values):
        """Set and validate all submitted form data."""
        for key in values:
            self[key].value = values[key]

    def validate(self, values):
        erred = False
        for key in values:
            try:
                self[key].validate(values[key])
            except Invalid:
                erred = True

        if erred:
            raise Invalid()

    def __getitem__(self, name):
        """Return the field of the corresponding name."""
        return self.fields[name]


    def __call__(self):
        """Render all the fields."""
        fields = []
        for name in self.fields:
            field = self[name].__html__()
            fields.append(field)
        return ''.join(fields)

    def __html__(self):
        """For the sake of templating engines."""
        return self()
