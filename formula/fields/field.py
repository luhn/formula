

class Field(object):
    parent = None

    def __init__(self, name, label=None, placeholder=None):
        self.name = name
        self.label = label
        self.placeholder = placeholder
