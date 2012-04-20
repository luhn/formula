from validator import Validator
from formula.exceptions import Invalid

class Numeric(Validator):
    msg = 'You must enter a number.'

    def __call__(self, value):
        if value:
            try:
                return float(value)
            except ValueError:
                raise Invalid(self.msg)
