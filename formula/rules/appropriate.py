import os.path

from rule import Rule
from formula.exceptions import Invalid

class Appropriate(Rule):
    msg = 'Keep it appropriate, please!'
    words = []

    def __call__(self, value):
        list = value.split()
        for w in list:
            if w.lower() in self.words:
                raise Invalid(self.msg)

__dir__ = os.path.dirname(os.path.abspath(__file__))
for w in open(os.path.join(__dir__, 'badwords.txt')):
    Appropriate.words.append(w.strip().lower())

