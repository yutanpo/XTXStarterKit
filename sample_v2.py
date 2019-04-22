import time
import subprocess

def get_data():
    return input()

def submit_prediction(pred):
    print(str(pred))

### YOUR CODE BELOW

while(True):
    try:
        ### Get next line of data
        data = get_data()

        ### Guess 0 every time
        submit_prediction(0)
    except EOFError as e:
        break;
