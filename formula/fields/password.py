from base_input import Input

class Password(Input):
    """A password input."""
    type = 'password'

    def __html__(self):
        """Make sure the field is rendered with no value."""
        self.value = ''
        return Input.__html__(self)

