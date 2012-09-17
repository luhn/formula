import re

from rule import Rule
from formula.exceptions import Invalid

class Regex(Rule):
    """Validate that a field conforms to the specified regex."""

    msg = 'Invalid input.'

    def __init__(self, regex, msg=None):
        self.regex = regex
        Rule.__init__(self, msg)

    def __call__(self, value):
        if value:
            if not re.match(self.regex, value):
                raise Invalid(self.msg)

