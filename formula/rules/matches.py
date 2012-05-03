from rule import Rule
from formula.exceptions import Invalid

class Matches(Rule):
    """Confirm field matches another field."""

    def __init__(self, field, msg=None):
        self.field = field
        if not msg:
            self.msg = 'This field must match the '+field.label+' field.'
        else:
            self.msg = msg

    def __call__(self, value):
        if value:
            if value!=self.field.value:
                raise Invalid(self.msg)
