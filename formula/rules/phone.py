import re

from rule import Rule
from formula.exceptions import Invalid

class Phone(Rule):
    """Validate a 10-digit phone number.  By passing an area_code argument to
    __init__(), the validator will automatically prepend it to a 7-digit phone
    number."""

    msg = 'Must be a 10-digit phone number.'

    def __init__(self, msg=None, area_code=None):
        if msg:
            self.msg = msg
        print area_code
        self.area_code = str(area_code)

    def __call__(self, value):
        if value:
            new = re.sub(r'[^0-9]+', '', value)
            if len(new)==7 and self.area_code:
                new = self.area_code + new
            if not len(new)==10:
                raise Invalid(self.msg)
            return new
