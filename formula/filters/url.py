from urlparse import urlparse

from filter import Filter
from formula.exceptions import Invalid

class URL(Filter):
    """Prepend http:// if it's not a valid URL."""

    def __call__(self, value):
        if value:
            scheme = urlparse(value).scheme
            if not (scheme=='http' or scheme=='https'):
                return 'http://'+value
        return value
