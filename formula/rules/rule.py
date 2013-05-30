
class Rule(object):
    def __init__(self, msg=None):
        if msg is None:
            self.msg = self.default_msg
        else:
            self.msg = msg

    @property
    def default_msg(self):
        raise NotImplementedError()

    def __call__(self, value):
        raise NotImplementedError()

