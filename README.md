CherryCutter
============

A minimal cookiecutter template for a minimal framework, CherryPy.

Cherrypy is amazing and very tiny; in fact, it's really, really tiny. I often find myself writing the same boilerplate code over and over, using the same modules, and building the same structure.

Enter cookiecutter!

This is an opinionated template that inclues PeeWee, Jinja2, and CherryPy for bootstraping a small site or a microservice. If you'd like to use a template without them, feel free to fork and customize away :)

Requirements
------------
You will need cookiecutter installed to use this template
`pip install cookiecutter`

In addition, the requirements.txt file only works with Python3. You may need different versions if you need Python 2.7 support (why haven't you migrated yet?).

Usage
-----
Generate a new Cookiecutter template layout: 
`cookiecutter gh:madelyneriksen/cookiecutter-cherrycutter`

Install Requirements:
```
cd yourprojectslug
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```
Run the App:
```
python cli.py
```

Visit "localhost:8080/" in your browser for a "Hello World!"


License
-------
This project is licensed under the terms of the [MIT License](/LICENSE)
