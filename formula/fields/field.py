

class Field(object):
    parent = None

    def __init__(self, name, label=None, placeholder=None, value=None):
        self.name = name
        self.label = label
        self.placeholder = placeholder
        self.value = value

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
