### XTX Prediction Challenge

## Instructions

The goal of this challenge is to create a program to predict stock movement based on real-market orderbook data. You have been provided a dateset and some starter code to help you  

## data.csv
* This file contains some data for you to analyze and train your model. 
* The goal of the challenge is to be able to predict the y values (the column on the far right), using only previous rows. 
* You should keep in mind that your model will be tested on data which is similar to `data.csv`, however it does not contain the y column.

## sample.py
* Use this file if you are writing your program in Python.
* This file contains the starter code for your program.
* Use the function `get_next_data()` to read a line of data.
* Use the function `submit_prediction(pred)` to submit your prediction for the y value of the next row of data.
* You cannot call `get_next_data()` twice in a row without calling `submit_prediction(pred)`.

## sample.r
* Use this file if you are writing your program in R.
* This file contains the starter code for your program.
* Use the function `get_next_data()` to read a line of data.
* Use the function `submit_prediction(pred)` to submit your prediction for the y value of the next row of data.
* You cannot call `get_next_data()` twice in a row without calling `submit_prediction(pred)`.

## model_tester.py
* This program is used to test your model by running `python3 model_tester.py`
* A prediction vector will be outputted at the value of RESULT_LOCATION
* Any changes you make to this file will not persist on the testing servers

## scorer.py
* This program is used to score a prediction vector
* Point the program to your prediction vector with RESULT_LOCATION
* Point the program at the dataset used to create the prediction vector with DATASET_LOCATION
* This program will print your r2 value to stdout after running with `python3 scorer.py` 
