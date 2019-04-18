import time
import subprocess

def get_data():
    return input()

def submit_prediction(pred):
    print(str(pred))

while(True):
    data = get_data()
    with open("blah.txt", "a+") as wp:
        wp.write(data + '\n')

    submit_prediction(data)
