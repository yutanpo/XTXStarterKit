### OSX/Linux Virtual Environment Setup (Python)

#### Setting up a virtual environment & installing requirements.txt packages

We highly recommend setting up a virtual environment before running the `run_tester_python.py` script.

The main purpose of a Python virtual environment is to create an isolated environment for Python projects.

Run the following commands from within the `python` directory to setup a Python virtual environment:

#### install virtualenv
$ python3 -m pip install --user virtualenv

#### creating a virtual environment
$ python3 -m venv env

#### activating a virtual environment
$ source env/bin/activate

#### install packages from requirements.txt
$ pip3 install -r requirements.txt
