# Intro

This is a little tutorial designed to get you on your feet with formula.

We'll start off with the most basic of forms, a single simple text field.

```python
>>> import formula
>>> field = formula.Text('my_field')
>>> field.render()
'<input type="text" name="my_field" value="" />'
```

And it works straight out of the box with most templating engines!  For example, in Chameleon, the following code in tandem with what we just wrote will display our field on the webpage.

```html
<html>
<body>
${field}
<!-- That will output the following: -->
<input type="text" name="my_field" value="" />
</body>
</html>
```

We can easily add any HTML attributes we desire.

```python
>>> field = formula.Text('my_field', value='Foo', placeholder='Bar', class=['baz', 'bop'])
>>> field.render()
'<input type="text" name="my_field" value="Foo" placeholder="Bar" class="baz bop" />'
```

And let's not forget about labels.

```python
>>> field = formula.Text('my_field', label='My field')
>>> field.label.render() + ' ' + field.render()
'<label for="my_field">My field</label> <input type="text" name="my_field" id="my_field" />'
>>> field.wrapper.render()
'<label>My field <input type="text" name="my_field" /></label>'
```

You'll notice that there's `field.label` and `field.wrapper`.  What's up with that?  `field.wrapper` is a label tag with the field inside it.  `field.label` is a standalone label tag.

## Rules and filters

Form validation is a very useful tool.  This can be done using formula's rules.  For example:

```python
>>> field = formula.Text('username')
>>> field.rules = [ formula.Required, # They cannot leave the field blank
>>>         formula.Length(8, 12), # Must be between 8 and 12 characters
>>>         formula.Characters(formula.ALPHANUMERICAL), # Only letters and numerals allowed
>>>         ]
```

You can see **a full list of rules** or even **make your own rules**.  Now, let's have somebody enter something into our form.

```python
>>> field.validate('Foobar') # Too short
Exception:  formula.exceptions.Invalid
>>> field.render()
'<input type="text" name="username" value="Foobar" class="error" data-rules="{'required':true,'length':[8,12],'characters':'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'}" />'
>>> field.errors.render()
'<span class="errors">Must be between 8 and 12 characters.</span>'
```

Now, you probably noticed the `data-rules` attribute.  What's that all about?  It's so the rules can be enforced client-side as well as server-side.  Read more about **client-side validation**.

