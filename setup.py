from setuptools import setup, find_packages

setup(
    name = 'ToWXR',
    version = '0.1',
    description = 'Generate WordPress Extended RSS files from various formats.',
    long_description = "Currently supported formats are CSV1.",
    classifiers = [], # Get strings from http://pypi.python.org/pypi?%3Aaction = list_classifiers
    keywords = 'wordpress wxr import export generate csv',
    author = 'Alexander Artemenko',
    author_email = 'svetlyak.40wt@gmail.com',
    url = 'http://anonymous.ag',
    license = 'MIT License',
    packages = find_packages(),
    install_requires = [
        'elementflow >= 0.3',
        'opster',
    ],
    entry_points = {
        'console_scripts': ['towxr = towxr:main']
    }
)
