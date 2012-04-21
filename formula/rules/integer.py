from rule import Rule
from formula.exceptions import Invalid

class Integer(Rule):
    """Validate that field is an integer."""

    msg = 'You must enter a whole number.'

    def __call__(self, value):
        if value:
            try:
                return int(value)
            except ValueError:
                raise Invalid(self.msg)
