from rule import Rule
from formula.exceptions import Invalid

class Natural(Rule):
    """
    Validate that field is a natural number, that is, a positive integer. Zero
    is by default allowed, but can be disallowed with Natural(zero=False)
    """

    msg = 'You must enter a whole number'

    def __init__(self, msg=None, zero=True):
        if msg:
            self.msg = msg
        else:
            self.msg = 'You must enter a whole number '
            if zero:
                self.msg += 'zero or greater.'
            else:
                self.msg += 'greater than zero.'
        self.zero = zero

    def __call__(self, value):
        if value:
            try:
                num = int(value)
            except ValueError:
                raise Invalid(self.msg)
            if not num >= 0:
                raise Invalid(self.msg)
            if not self.zero and num==0:
                raise Invalid(self.msg)
            return num
