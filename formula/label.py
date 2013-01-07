from formula.html import Tag, TagContent

class Label(object):
    """An object representing a <label> tag.  Can be used as either a label or
    a wrapper.  See _____ for the distinction between labels and wrappers."""
    def __init__(self, text, align='left'):
        self.text = text
        if align not in ['left', 'right']:
            raise ValueError('Align must be left or right.')
        self.align = align

    def label(self, field):
        return Tag('label', self.text, for_=field.id)

    def wrap(self, tag, field):
        if self.align == 'left':
            args = [self.text, ' ', tag]
        else:
            args = [tag, ' ', self.text]
        return Tag('label', TagContent(*args), for_=field.id)


