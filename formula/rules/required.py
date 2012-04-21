from rule import Rule
from formula.exceptions import Invalid

class Required(Rule):
    msg = 'This field is required.'

    def __call__(self, value):
        if not value:
            raise Invalid(self.msg)
