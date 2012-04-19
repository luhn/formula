from validator import Validator
from formula.exceptions import Invalid

class Required(Validator):
    msg = 'This field is required.'

    def __call__(self, value):
        if not value:
            raise Invalid(self.msg)
