
def no_renderer(field, html):
    return html

def basic_renderer(field, html):
    r = ['<p']
    if field.errors:
        r.append(' class="error"')
    r.append('>')
    if field.label:
        r.append('<label for="')
        if field.parent_name:
            r.extend([field.parent_name, '_'])
        r.extend([field.name, '">', field.label, '</label>'])
    r.append(html)
    if field.errors:
        r.extend(['<span class="error">', field.escape(field.errors[0]),
            '</span>'])
    r.append('</p>')
    return ''.join(r)
