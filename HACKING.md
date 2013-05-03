# Hacking

Want to fix a bug or add a feature?  Sweet!  Let's get you set up.

```
$ git clone https://github.com/luhn/formula.git
$ cd formula/
$ python setup.py develop
```

## Testing

You'll need to make sure all the tests pass and, as you develop, continue to pass.

```
$ python tests/
```

You should see some output.  Make sure it ends with "OK".

## Test coverage

As you develop, you'll need to write tests for your new code and ensure 100% test coverage.  You can use Python's `coverage` package (`pip install coverage`) to measure the test coverage.

```
$ coverage run tests/__main__.py
$ coverage report
```

Make sure that it's nothing but 100% under the `Cover` column.  If it isn't, you can generate more detailed reports.

```
$ coverage html
$ open htmlcov/index.html
```
