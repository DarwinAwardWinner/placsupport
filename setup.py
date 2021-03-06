import os
from setuptools import setup, find_packages

def read_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "placsupport",
    version = "0.1dev",
    packages = find_packages(),

    # metadata for upload to PyPI
    author = "Ryan C. Thompson",
    author_email = "rct@thompsonclan.org",
    description = "Support functions for using plac",
    license = "BSD",
    keywords = ("plac", "argparse"),
    #url = "http://example.com/HelloWorld/",   # project home page, if any
    long_description = read_file('README.md'),
    url='https://github.com/DarwinAwardWinner/placsupport/',

    # Dependencies
    install_requires = [],
    requires = ['plac'],
)
