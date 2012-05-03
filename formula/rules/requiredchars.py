import re

from rule import Rule
from formula.exceptions import Invalid

class RequiredChars(Rule):
    """Confirm that the field contains at least one instance of the required
    characterss."""

    UPPER = 1
    LOWER = 2
    NUM = 4

    def __init__(self, required, msg):
        self.msg = msg
        self.required = required

    def __call__(self, value):
        if value:
            if self.required & self.UPPER and not re.search('[A-Z]', value):
                raise Invalid(self.msg)
            if self.required & self.LOWER and not re.search('[a-z]', value):
                raise Invalid(self.msg)
            if self.required & self.NUM and not re.search('[0-9]', value):
                raise Invalid(self.msg)

