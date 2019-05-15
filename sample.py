import time
import subprocess
import sys

def get_next_data():
    """
    Reads input from standard input

    Use this to supply your model with input
    Input will not be supplied until output is 
    generated for the previous input
    """
    return input()

def submit_prediction(prediction):
    """
    Submits your prediction to standard output
    """
    print(str(prediction))

def eprint(msg):
    """
    Prints to standard error

    Use this to debug / develop. 
    This output will not be scored
    """
    print(msg, file=sys.stderr)

### YOUR CODE BELOW

while(True):
    try:
        ### Get next line of data
        data = get_next_data()

        ### Guess 0 every time
        submit_prediction(0)
    except EOFError as e:
        break
