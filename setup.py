
from setuptools import setup

setup(
    name='formula',
    version='1.0',
    description='',
    author='Theron Luhn',
    author_email='theron@luhn.com',
    packages=[
        'formula',
        'formula.fields',
        'formula.filters',
        'formula.rules',
        'formula.renderers',
        'formula.test',
        ],
    package_data={'formula.rules': ['badwords.txt']},
    requires=[
    ],
    )
