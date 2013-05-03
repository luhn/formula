from formula.html import Tag, TagContent
from formula.label import Label

class Text(object):
    """A text input."""

    def __init__(self, name, value=None, label=None, wrapper=None, id=None,
            **kwargs):
        self.name = name
        self.value = str(value) if value is not None else ''
        if id is True:
            self.id = True
        else:
            self._id = id
        if isinstance(label, basestring):
            self.label = Label(label)
        else:
            self.label = label
        if isinstance(wrapper, basestring):
            self.wrapper = Label(wrapper)
        else:
            self.wrapper = wrapper
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

    def prerender(self):
        """Return a Tag or TagContent object."""
        tag = Tag('input', type_='text', name=self.name, value=self.value,
                id=self._id)
        tag.set_attributes(self.attributes)
        if self.label:
            if self.label.align == 'left':
                args = [self.label.label(self), ' ', tag]
            else:
                args = [tag, ' ', self.label.label(self)]
            tag = TagContent(*args)
        if self.wrapper:
            tag = self.wrapper.wrap(tag, self)
        return tag

    def render(self):
        return self.prerender().render()

    def __html__(self):
        return self.render()

