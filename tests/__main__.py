import unittest

if __name__ == '__main__':

    try:
        import bs4
    except ImportError:
        print 'Testing Formula requires Beautiful Soup 4.'
        print 'Install Beautiful Soup 4 with `pip install beautifulsoup4`'
        exit()

    from html import TestHtmlClasses
    from fields import TestFields
    from rules import TestRules

    unittest.main()

