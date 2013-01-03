HTML will be rendered by two classes, Tag and TagContent.

## Basic use

A single field

```python
import formula
print formula.Text('email').render()
# Output: <input type="text" name="email" />
```

Labels and custom attributes

```python
print formula.Text('email', label='Email', id_='email_field').render()
# Output: <label>Email <input type="text" name="email" id="email_field" /></label>
```

Works in templating engines too (by using __html__() method):

```html
<p>${formula.Text('email')}</p>
```

Validation:

```python
field = formula.Text('email')
field.rules(formula.Required, formula.Email)
if(field.validate('')) {
    print 'Passed'
} else {
    print 'Error: ' + field.error
}
# Output: Error: This field is required.
```

Multiple fields to make up a form:

```python
form = formula.Form('contact_info')
form.name = formula.Text(label='Name') #Name is assumed from attribute name
form.is_robot = formula.Checkbox(label='I am a robot')
for field in form:
    print field.render()
# Output:
# <label>Name <input type="text" name="name" /></label>
# <label><input type="checkbox" name="is_robot" /></label>
```

Or output the entire form at once:  (You can define the wrapper tag.)

```python
form.render()
# Output:
# <p><label>Name <input type="text" name="name" /></label></p>
# <p><label><input type="checkbox" name="is_robot" /></label></p>
```

Plenty of hooks for plugins:

```python
class MyPlugin(formula.Plugin):
    def render_field(self, tag, field):
        tag.classes.append('awesomesauce')
        return tag

# The plugin argument also works with formula.Form()
print formula.Text('email', plugin=MyPlugin).render()
# Output: <input type="text" name="email" class="awesomesauce" />
```
