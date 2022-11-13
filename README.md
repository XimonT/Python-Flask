# Python-Flask
all you need to now to work with flask

---

## Create a Virtual Enviroment

Virtual environments enable you to have an isolated space on your server for Python projects. We’ll use venv, part of the standard Python 3 library, which we can install by typing:

`sudo apt install -y python3-venv`

Here, we’ll call our new environment "my_env"

`python3 -m venv my_env`

Activate the environment using the command below

`source my_env/bin/activate`

Deactivate the environment using the command below

`deactivate`

---

## Run the Flask application

In a terminal, you will set the FLASK_APP and FLASK_DEBUG values from within the Virtual Enviroment:

`export FLASK_APP=project`
`export FLASK_DEBUG=1`

The FLASK_APP environment variable instructs Flask on how to load the app. You would want this to point to where create_app is located. For this tutorial, you will be pointing to the project directory.

The FLASK_DEBUG environment variable is enabled by setting it to 1. This will enable a debugger that will display application errors in the browser.

Ensure that you are in the main directory and then run the project:

`flask run`
