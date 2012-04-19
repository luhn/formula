

def twitter_bootstrap(field, html):
    """Render a single field."""
    r = ['<div class="control-group']
    if field.errors:
        r.append(' error')
    r.append('">')
    if field.label:
        r.append('<label class="control-label" for="')
        if field.parent_name:
            r.extend([field.parent_name, '_'])
        r.extend([field.name, '">', field.label, '</label>'])
    r.extend(['<div class="controls">', html])
    if field.errors:
        r.extend(['<span class="help-inline">', field.escape(field.errors[0]),
            '</span>'])
    r.append('</div></div>')
    return ''.join(r)
