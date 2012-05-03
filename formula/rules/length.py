from rule import Rule
from formula.exceptions import Invalid

class Length(Rule):
    """Confirm field is the proper length."""

    def __init__(self, min, max=None, msg=None):
        self.min = min
        self.max = max
        if msg:
            self.msg = msg
        elif max:
            self.msg = 'The field must be between '+str(min)+' and '+str(max)\
                    +' characters in length.'
        else:
            self.msg = 'The field must be at least '+str(min)+' characters'

    def __call__(self, value):
        if value:
            if len(value)<self.min:
                raise Invalid(self.msg)
            if self.max and len(value)>self.max:
                raise Invalid(self.msg)

