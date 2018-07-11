"""
Main entrypoint for the web app {{ cookiecutter.project_name }}
"""

import cherrypy
from jinja2 import Environment, FileSystemLoader
from {{ cookiecutter.project_slug }} import models

# Constants
JENV = Environment(loader=FileSystemLoader('templates'))

class Root:
    @cherrypy.expose
    def index(self):
        template = JENV.get_template('index.html')
        return template.render()

if __name__ == "__main__":
    cherrypy.quickstart(Root(), '/', '{{ cookiecutter.project_slug }}/app.conf')
