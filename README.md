# XTX Markets Forecasting Challenge

## Instructions

The goal of this challenge is to create a program to predict stock movement based on real-market orderbook data. A dataset and some starter code has been provided to help build submissions.

## data.csv
* We have included a small sample of the dataset in this starter kit. The full dataset can be downloaded [here](https://www.google.com/search?rlz=1C5CHFA_enUS835US836&ei=FcHiXPuEOsTO5gLG-ayYBw&q=insert+file+download+link+here&oq=insert+file+download+link+here&gs_l=psy-ab.3...4342.5057..5172...0.0..0.130.481.3j2......0....1..gws-wiz.......0i71j35i39.wmmOJos0Zbs).
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

Ensure that all development is being done within the `python` folder. 

Objects that are required for your submission to run successfully such as: models, files that you create must be stored in `python`. 

At all phases of the development process it is highly recommended to run `./run_tester_python.sh` from within the `python` directory.

If your submission is not able to run with `./run_tester_python.sh` it will NOT run on our platform.

This script will ensure that submission folder is in accordance with:  

|--README.md
|-- python
   |-- core.py
   |-- requirements.txt
   |-- run_tester_python.sh
   |-- submission.py
|-- r
   |-- requirements.txt
   |-- submission.r
|-- src
   |-- model_tester.py
   |-- scorer.py
|-- data.csv
|--README.md
|-- python
   |-- core.py
   |-- requirements.txt
   |-- run_tester_python.sh
   |-- submission.py
|-- r
   |-- requirements.txt
   |-- submission.r
|-- src
   |-- model_tester.py
   |-- scorer.py
|-- data.csv


Additionally, `./run_tester_python.sh` will also run `src/model_tester.py`, and return a score. 

The result & score can be found in the results folder that will be created upon successfully running `./run_tester_python.sh`.

### R

Ensure that all development is being done within the `r` folder. 

Objects that are required for your submission to run successfully such as: models, files that you create must be stored in `r`. 

At all phases of the development process it is highly recommended to run `./run_tester_r.sh` from within the `r` directory.

If your submission is not able to run with `./run_tester_r.sh` it will NOT run on our platform.

This script will ensure that submission folder is in accordance with:  

|--README.md
|-- python
   |-- core.py
   |-- requirements.txt
   |-- run_tester_python.sh
   |-- submission.py
|-- r
   |-- requirements.txt
   |-- submission.r
|-- src
   |-- model_tester.py
   |-- scorer.py
|-- data.csv
|--README.md
|-- python
   |-- core.py
   |-- requirements.txt
   |-- run_tester_python.sh
   |-- submission.py
|-- r
   |-- requirements.txt
   |-- submission.r
|-- src
   |-- model_tester.py
   |-- scorer.py
|-- data.csv


Additionally, `./run_tester_r.sh` will also run `src/model_tester.py`, and return a score. 

The result & score can be found in the results folder that will be created upon successfully running `./run_tester_r.sh`.


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
* **Any packages or dependencies necessary for the submission should be added here.**
* These will be installed at runtime.

### Submission Instructions

#### For Python submissions

Before submitting, it is highly recommended to run `./run_tester_python.sh` from within the `python` directory
A submissiong that doesn't work with `./run_tester_python.sh` will get rejected

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

Before submitting, it is highly recommended to run `./run_tester_r.sh` from within the `r` directory
A submissiong that doesn't work with `./run_tester_r.sh` will get rejected

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
