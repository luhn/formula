from formula.html import Tag, TagContent

class Text(object):
    """A text input."""

    def __init__(self, name, value=None, label=None, **kwargs):
        self.name = name
        self.value = str(value) if value is not None else ''

        """Some special code for `id`.  If it's explicitly set, use that.
        Otherwise the default value varies on if there's a label of not."""
        if 'id' in kwargs:
            self.id = kwargs['id']
            del kwargs['id']
        else:
            if label:
                self.id = True
            else:
                self.id = None

        self._label = label

        self.attributes = kwargs

    @property
    def id(self):
        """The ``id`` property is interesting.  You can set it via __init__ or
        directly, and it will render in the tag.  However, if you set it as
        True, an id will automatically be created for you.  Moreover, even
        accessing this property with the id not set will automatically set it.

        """
        if not self._id:
            self.id = True
        return self._id

    @id.setter
    def id(self, value):
        if value is True:
            self._id = self.name
        else:
            self._id = value

    @property
    def label(self):
        """Return a ``<label>`` tag for use with the field."""
        if not self._label:
            raise ValueError('No label set.')
        return Tag('label', for_=self.id, content=self._label)

    @property
    def wrapper(self):
        """Return a ``<label>`` tag with the field inside."""
        return self._wrapper('left')

    @property
    def right_wrapper(self):
        """Same as ``wrapper``, but the text is to the right of the field."""
        return self._wrapper('right')

    def _wrapper(self, align):
        if not self._label:
            raise ValueError('No label set.')
        if align == 'left':
            content = [ self._label, ' ', self ]
        else:
            content = [ self, ' ', self._label ]
        return Tag('label', for_=self.id, content=content)


    def prerender(self):
        """Return a Tag or TagContent object."""
        tag = Tag('input', type_='text', name=self.name, value=self.value,
                id=self.id)
        tag.set_attributes(self.attributes)
        return tag

    def render(self):
        return self.prerender().render()

    def __html__(self):
        return self.render()

