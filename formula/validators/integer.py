from validator import Validator
from formula.exceptions import Invalid

class Integer(Validator):
    msg = 'You must enter a whole number.'

    def __call__(self, value):
        if value:
            try:
                return int(value)
            except ValueError:
                raise Invalid(self.msg)
