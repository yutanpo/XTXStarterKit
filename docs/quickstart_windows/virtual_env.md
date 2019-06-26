### Windows Virtual Environment Setup (Python)

# Setting up a virtual environment & installing requirements.txt packages

We highly recommend setting up a virtual environment before running the `run_tester_python.py` script.

The main purpose of a Python virtual environment is to create an isolated environment for Python projects.

Run the following commands from within the `python` directory to setup a Python virtual environment:

# install virtualenv
$ py -m pip install --user virtualenv

# creating a virtual environment
$ py -m venv env

# activating a virtual environment
$ .\env\Scripts\activate

# install packages from requirements.txt
$ py -m pip install -r requirements.txt
