from exceptions import Invalid
from renderers import basic_renderer
from collections import OrderedDict

class Form(object):
    """An object that stores all the fields of the form."""

    def __init__(self, name, renderer = None):
        self.fields = OrderedDict()
        self.name = name
        if renderer == None:
            renderer = basic_renderer
        self.renderer = renderer

    def add(self, field):
        """Add a new field."""
        name = field.name
        if not field.renderer:
            field.renderer = self.renderer
        field.parent_name = self.name
        self.fields[name] = field
        return field

    def set_values(self, values):
        """Set and validate all submitted form data."""
        for key in values:
            self[key].value = values[key]

    def get_values(self):
        """Get the values from the form data."""
        values = {}
        for key in self.fields:
            values[key] = self.fields[key].value
        return values

    values = property(get_values, set_values)

    def validate(self, values):
        erred = False
        for key in values:
            try:
                self[key].validate(values[key])
            except KeyError:
                pass
            except Invalid:
                erred = True

        if erred:
            raise Invalid()

    def __getitem__(self, name):
        """Return the field of the corresponding name."""
        return self.fields[name]

    def __setitem__(self, name, value):
        """Set the value of the field with the corresponding name."""
        self.fields[name].value = value


    def __call__(self):
        """Render all the fields."""
        fields = []
        for field in self.fields.itervalues():
            fields.append(field.__html__())
        return ''.join(fields)

    def range(self, start, end):
        """Render all fields between the fields of start and end"""
        class RangeMaker(object):
            def __init__(self, fields, start, end):
                self.start = start
                self.end = end
                self.fields = fields

            def __html__(self):
                appending = False
                fields = []
                for key, field in self.fields.iteritems():
                    if key==self.start:
                        appending = True
                    elif key==self.end:
                        break
                    if appending:
                        fields.append(field.__html__())
                return ''.join(fields)

        return RangeMaker(self.fields, start, end)

    def __html__(self):
        """For the sake of templating engines."""
        return self()
