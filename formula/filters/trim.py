from filter import Filter
from formula.exceptions import Invalid

class Trim(Filter):
    """Remove all whitespace before and after the value."""

    def __call__(self, value):
        return value.strip()
