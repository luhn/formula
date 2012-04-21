from formula import Form
from formula.fields import Text
from formula.rules import Required, Natural
from formula.filters import Trim
from formula.exceptions import Invalid

#Create a basic form
f = Form('my_form')
f.add(Text('text'))
f.add(Text('text2', placeholder='Some Text'))

print f()

#Submit some data
post = {
    'text': 'Hello, world.',
    'text2': 'More text'
    }
f.values(post)

print f()

#Add some validators
f['text'].rules(Required(), Natural(zero=False))
f['text'].filters(Trim())
try:
    f.validate({ 'text': ' 0 ' })
except Invalid:
    pass

print f()
