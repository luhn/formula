from urlparse import urlparse

from rule import Rule
from formula.exceptions import Invalid

class URL(Rule):
    """Validate that field is not an empty string."""

    msg = 'This field must be a valid URL.'

    def __call__(self, value):
        if value:
            scheme = urlparse(value).scheme
            if not (scheme=='http' or scheme=='https'):
                raise Invalid(self.msg)

