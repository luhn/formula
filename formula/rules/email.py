import re

from rule import Rule
from formula.exceptions import Invalid

class Email(Rule):
    """Validate that field is a valid email address."""

    msg = 'Not a valid email.'

    def __call__(self, value):
        if value:
            if not re.match(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$',
                    value):
                raise Invalid(self.msg)
