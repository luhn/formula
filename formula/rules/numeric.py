from rule import Rule
from formula.exceptions import Invalid

class Numeric(Rule):
    """Validate that field is a numeral value."""

    msg = 'You must enter a number.'

    def __call__(self, value):
        if value:
            try:
                return float(value)
            except ValueError:
                raise Invalid(self.msg)
