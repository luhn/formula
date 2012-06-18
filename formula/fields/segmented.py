from field import Field

class Segmented(Field):
    """A segmented control unique to Twitter Bootstrap."""
    def __init__(self, name, options, **kwargs):
        self.options = options
        Field.__init__(self, name, **kwargs)

    def __html__(self):
        r = ['<div class="btn-toolbar">',
                '<div class="btn-group" id="', self.id(), '">']
        for option in self.options:
            r.extend(['<a href="#" data-value="', self.escape(str(option)),
                '" class="btn'])
            if str(option)==str(self.value):
                r.append(' active')
            r.append('">')
            #If it's a dictionary, get the text, otherwise use the value
            if isinstance(self.options, dict):
                r.append(self.escape(str(self.options[option])))
            else:
                r.append(self.escape(str(option)))
            r.append('</a>')

        r.extend(['</div></div>',
            '<input type="hidden" name="', self.name, '" id="', self.id(),
            '_hidden" value="', str(self.value), '" />'])
        r.append("""
        <script type="text/javascript">
        $(function() {
            $('#%s a').live('click', function(e) {
                $(this).parent().children().removeClass('active');
                $(this).addClass('active');
                $('#%s_hidden').val($(this).data('value'));
                e.preventDefault();
            });
        });
        </script>
        """ % (self.id(), self.id()))
        return self.renderer(self, ''.join(r))
