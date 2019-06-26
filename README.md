# XTX Markets Forecasting Challenge

## Instructions

The goal of this challenge is to create a program to predict stock movement based on real-market orderbook data. A dataset and some starter code has been provided to help build submissions.

## data.csv
* A small sample of the dataset is included in this starter kit. The full dataset can be downloaded [here](https://storage.googleapis.com/xtx-public-assets/data-training.csv.zip).
* After downloading the dataset, it can be included in the root of the StarterKit directory, but it **should not** be included in the final submission.
* This file contains some data to be analyzed and trained with the submitted model. 
* The goal of the challenge is to predict the y values (the column on the far right), given the current and all past rows. 
* The submitted model will be tested on data which is similar to `data.csv`; however it will not contain the y column.

### StarterKit Folder Structure

There are two programming languages that are currently supported for this challenge, Python and R.

In this challenge, There are three relevant folders - one named `src` containing all the source code needed to process data 
files and getting your result, another two named either `python` or `r` depending on preference of language to be used in the 
submission. The first step should be to choose a programming language by removing the folder that is unnecessary for the 
submission. For example, if the language used in a submission is `python`, the `r` folder should be removed.

### Quickstart

### Python

Requirements: Python 3.6 or higher

Objects that are required for your submission to run successfully such as: models, files that you create must be stored in `python`.

Place required Python packages in the `requirements.txt` file. These packages will be installed on the fly on our submission environment.

With that being said, our testing script `run_tester_python.py` will NOT install these packages; therefore, please ensure your system has the packages installed in order to test locally.

### Windows

## Setting up a virtual environment & installing requirements.txt packages

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

At all phases of the development process it is highly recommended to run `py run_tester_python.py` from within the `python` directory.

If your submission is not able to run with `py run_tester_python.py`, it will NOT run on our platform.

This script will ensure that the submission folder satisfies:  

|--README.md
|-- python
   |-- core.py
   |-- requirements.txt
   |-- run_tester_python.sh
   |-- submission.py
|-- src
   |-- model_tester.py
   |-- scorer.py
|-- data.csv
|-- data-training.csv

Additionally, `py run_tester_python.py` will also run `src/model_tester.py`, and return a score. 

The result & score can be found in the results folder that will be created upon successfully running `py run_tester_python.py`.

### macOS and Linux

## Setting up a virtual environment & installing requirements.txt packages

We highly recommend setting up a virtual environment before running the `run_tester_python.py` script.

The main purpose of a Python virtual environment is to create an isolated environment for Python projects.

Run the following commands from within the `python` directory to setup a Python virtual environment:

# install virtualenv
$ python3 -m pip install --user virtualenv

# creating a virtual environment
$ python3 -m venv env

# activating a virtual environment
$ source env/bin/activate

# install packages from requirements.txt
$ pip3 install -r requirements.txt

At all phases of the development process it is highly recommended to run `python3 run_tester_python.py` from within the `python` directory.

If your submission is not able to run with `python3 run_tester_python.py`, it will NOT run on our platform.

This script will ensure that the submission folder satisfies:  

|--README.md
|-- python
   |-- core.py
   |-- requirements.txt
   |-- run_tester_python.sh
   |-- submission.py
|-- src
   |-- model_tester.py
   |-- scorer.py
|-- data.csv
|-- data-training.csv

Additionally, `python3 run_tester_python.py` will also run `src/model_tester.py`, and return a score. 

The result & score can be found in the results folder that will be created upon successfully running `python3 run_tester_python.py`.

### R

NOTE: we expect you to have python 3 installed in order to run `run_tester_r.py`. You will not need to make changes to `run_tester_r.py`, it is used to test your submission.

Please install Python 3 from [here](https://www.python.org/downloads/release/python-373/).

Also ensure that R is installed on your machine. Installation information can be found [here](https://www.andrewheiss.com/blog/2012/04/17/install-r-rstudio-r-commander-windows-osx/)

We require your system to be able to run `Rscript` commands.

Ensure that all development is being done within the `r` folder. 

Objects that are required for your submission to run successfully such as: models, files that you create must be stored in `r`. 

Place required R packages in the `requirements.txt` file. These packages will be installed on the fly on our submission environment. 

With that being said, our testing script `run_tester_r.py` will NOT install these packages; therefore, please ensure your system has the packages installed in order to test locally. 

## Windows

At all phases of the development process it is highly recommended to run `py run_tester_r.py` from within the `r` directory.

If your submission is not able to run with `py run_tester_r.py` it will NOT run on our platform.

This script will ensure that the submission folder satisfies:

|--README.md
|-- r
   |-- core.r
   |-- requirements.txt
   |-- submission.r
|-- src
   |-- model_tester.py
   |-- scorer.py
|-- data.csv
|-- data-training.csv

Additionally, `run_tester_r.py` will also run `src/model_tester.py`, and return a score. 

The result & score can be found in the results folder that will be created upon successfully running `py run_tester_r.py`.

## macOS and Linux

At all phases of the development process it is highly recommended to run `python3 run_tester_r.py` from within the `r` directory.

If your submission is not able to run with `python3 run_tester_r.py` it will NOT run on our platform.

This script will ensure that the submission folder satisfies:

|--README.md
|-- r
   |-- core.r
   |-- requirements.txt
   |-- submission.r
|-- src
   |-- model_tester.py
   |-- scorer.py
|-- data.csv
|-- data-training.csv

Additionally, `run_tester_r.py` will also run `src/model_tester.py`, and return a score. 

The result & score can be found in the results folder that will be created upon successfully running `python3 run_tester_r.py`.

### The `src` folder

**None of these files require changing**; however, there are a couple of files in this folder that are quite important to know.
**Please refrain from trying to run these files manually**; there is a script in the python and R folders that runs the model_tester and scorer

## `src/model_tester.py`
* A prediction vector will be outputted at the value of `RESULT_LOCATION`.
* Any changes made to this file will not persist on the testing servers.

## `src/scorer.py`
* This program is used to score a prediction vector.
* This program will print the final `r2` value to stdout after running.


### The Submission Folders

#### `python`

This folder should be removed if the solution is written in `R`.

##### `python/core.py`
* This file does not need to be modified
* This file contains the `Submission` class, all code to interact with `src/model_tester.py`

##### `python/submission.py`
* This file should be used if the solution is written in Python.
* This file contains the starter code for the submission program.
* This extends the `Submission` class found in `core.py`.
* The function `self.get_next_data()` **must** be used to read a line of data.
* The function `self.submit_prediction(pred)` **must** be used to submit a prediction for the y value of the next row of data.
* **`self.get_next_data()` cannot be called two or more times in a row without calling `self.submit_prediction(pred)`**.
* Messages should not be printed to stdout because `model_tester.py` will be looking for predictions from stdout.
* To debug, messages should be printed to stderr.

##### `python/requirements.txt`
* **Any packages or dependencies necessary for the submission should be added here.**
* These will be installed at runtime.

&nbsp;

#### `r`

This folder should be removed if the solution is written in `python`.

##### `r.submission.r`
* This file should be used if the solution is written in R.
* This file contains the starter code for the submission program.
* The function `get_next_data()` **must** be used to read a line of data.
* The function `submit_prediction(pred)` **must** be used to submit a prediction for the y value of the next row of data.
* **`get_next_data()` cannot be called two or more times in a row without calling `submit_prediction(pred)`**.
* Messages should not be printed to stdout because `model_tester.py` will be looking for predictions from stdout.
* To debug, messages should be printed to stderr.

##### `r/requirements.txt`
* **Any packages or dependencies necessary for the R submission should be added here.**
* These will be installed at runtime.

### Submission Instructions

#### For Python submissions

Follow these steps to upload a python submission:

##### Step 1
Match this directory structure.

     python
     ├── core.py (required)
     ├── submission.py (required)
     └── requirements.txt

##### Step 2
Zip the whole directory (i.e. `python.zip`)

##### Step 3
Upload this .zip file on the challenge submission page.

#### For R submissions

Follow these steps to upload an r submission:

##### Step 1
Match this directory structure.

     r
     ├── submission.r (required)
     └── requirements.txt

##### Step 2
Zip the whole directory (i.e. `r.zip`)

##### Step 3
Upload this .zip file on the challenge submission page.
