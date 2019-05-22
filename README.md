# XTX Markets Forecasting Challenge

## Instructions

The goal of this challenge is to create a program to predict stock movement based on real-market orderbook data. You have been provided a dateset and some starter code to help you.

## data.csv
* This file is not contained in this starterkit, please find the data [here](https://www.google.com/search?rlz=1C5CHFA_enUS835US836&ei=FcHiXPuEOsTO5gLG-ayYBw&q=insert+file+download+link+here&oq=insert+file+download+link+here&gs_l=psy-ab.3...4342.5057..5172...0.0..0.130.481.3j2......0....1..gws-wiz.......0i71j35i39.wmmOJos0Zbs)
* After downloading the dataset, you can include it in the root of the starterkit directory, but do **not** include it in your final submission.
* This file contains some data for you to analyze and train your model. 
* The goal of the challenge is to be able to predict the y values (the column on the far right), given the current and all past rows. 
* You should keep in mind that your model will be tested on data which is similar to `data.csv`, however it does not contain the y column.

### Starterkit Folder Structure

There are 2 programming languages that are currently supported for this challenge. In this challenge, you will find 3 relevant folders - one named `src` containing all the source code
you would need process data files and getting your result, another two named either `python` or `r` depending on your preference in language. Your first step should be to choose your
programming language by removing the folder you would not need. For example, if your language preference is `python`, you should remove the `r` folder.

### The `src` folder

None of these files require changing; however, there are a couple functions in this folder that are quite important to know.

## `scr/model_tester.py`
* This program is used to test your model by running `python3 src/model_tester.py`
* If your language preference is `R`, you must run `python3 src/model_tester.py r` instead.
* A prediction vector will be outputted at the value of `RESULT_LOCATION`
* Any changes you make to this file will not persist on the testing servers

## `src/scorer.py`
* This program is used to score a prediction vector
* Point the program to your prediction vector with `RESULT_LOCATION`
* Point the program at the dataset used to create the prediction vector with `DATASET_LOCATION`
* This program will print your `r2` value to stdout after running with `python3 src/scorer.py` 

### The Submission Folders

#### `python`

You should remove this folder if you are writing your solution in `R`.

##### `python/core.py`
* This file does not need to be modified
* This file contains the `Submission` class, all code to interact with `src/model_tester.py`

##### `python/submission.py`
* This file contains the starter code for your program.
* Extends the `Submission` class found in `core.py`
* Use the function `self.get_next_data()` to read a line of data.
* Use the function `self.submit_prediction(pred)` to submit your prediction for the y value of the next row of data.
* You cannot call `self.get_next_data()` twice or more in a row without calling `self.submit_prediction(pred)`.
* You should NOT print to stdout as `model_tester.py` will be looking for your predictions from stdout
* Print to stderr instead for debugging

##### `python/requirements.txt`
* List any packages you wish to be installed at runtime.

#### `r`

You should remove this folder if you are writing your solution in `python`.

##### `r.submission.r`
* Use this file if you are writing your program in R.
* This file contains the starter code for your program.
* Use the function `get_next_data()` to read a line of data.
* Use the function `submit_prediction(pred)` to submit your prediction for the y value of the next row of data.
* You cannot call `get_next_data()` twice in a row without calling `submit_prediction(pred)`.
* You should NOT print to stdout as `model_tester.py` will be looking for your predictions from stdout
* Print to stderr instead for debugging

##### `r/requirements.txt`
* List any packages you wish to be installed at runtime.
