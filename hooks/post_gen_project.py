"""
Post generation hooks for CherryPy.

Currently adds an absolute path to the project static dir
to app.conf
"""

from os.path import dirname, realpath

STATIC = """
[/static]
tools.staticdir.on = True
tools.staticdir.dir = "%s/static"
""" % dirname(realpath("{{ cookiecutter.project_slug }}"))

CONFIG = "{{ cookiecutter.project_slug }}/app.conf"

with open(CONFIG, 'w') as file:
    file.write(STATIC)


