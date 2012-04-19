from formula import Form
from formula.fields import Text

f = Form('my_form')
f.add(Text('value'))

print f.__html__()
