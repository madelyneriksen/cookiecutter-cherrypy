"""
Post generation hooks for CherryPy.

Currently adds an absolute path to the project static dir
to app.conf
"""

import re
import sys
from os.path import dirname, realpath


# Check the Slug works as a valid module name
CHECK_RE = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

SLUG_MOD = "{{ cookiecutter.project_slug }}"

if not re.match(CHECK_RE, SLUG_MOD):
    print('%s Is not a valid Python Name, please adjust.' % slugmod)
    sys.exit(1)

STATIC = """
[/static]
tools.staticdir.on = True
tools.staticdir.dir = "%s/static"
""" % dirname(realpath("{{ cookiecutter.project_slug }}"))

CONFIG = "{{ cookiecutter.project_slug }}/app.conf"

with open(CONFIG, 'w') as file:
    file.write(STATIC)


