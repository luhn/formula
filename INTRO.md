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
