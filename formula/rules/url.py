import re

from rule import Rule
from formula.exceptions import Invalid

class URL(Rule):
    """Validate that field is not an empty string."""
    def __init__(self, msg=None, add_http=False):
        if msg:
            self.msg = msg
        self.add_http = add_http

    msg = 'This field must be a valid URL.'

    #This regex makes sure it's either http:// or https://
    checker = re.compile(r'https?')
    #This regex strips any characters that don't belong in a URL
    stripper = re.compile(r'[^-A-Za-z0-9+&@#/%?=~_|!:,.;\(\)]')

    def __call__(self, value):
        if value:
            if self.add_http and value[0:4] != 'http':
                value = 'http://' + value
            value = self.stripper.sub('', value)
            if not self.checker.match(value):
                raise Invalid(self.msg)
            return value

