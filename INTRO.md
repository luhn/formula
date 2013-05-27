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

