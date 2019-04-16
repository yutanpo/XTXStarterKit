import time
import random
import subprocess


def follow(the_file):
    f = subprocess.Popen(['tail', '-F', the_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while(True):
        line = f.stdout.readline()
        yield line

incoming = follow('input.txt')

def get_data():
    return incoming.__next__()

def submit_prediction(pred):
    with open('output.txt', 'a+') as wp:
        wp.write(str(pred) + '\n')

### YOUR CODE BELOW

# Sample algorithm
while(True):
    # Read in data
    data = get_data()

    # Always guess 3
    submit_prediction(3)
