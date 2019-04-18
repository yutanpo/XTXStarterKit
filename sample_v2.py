import time
import subprocess

def get_data():
    return input()

def submit_prediction(pred):
    print(str(pred))

while(True):
    try:
        data = get_data()
        with open("blah.txt", "a+") as wp:
            wp.write(data + '\n')

        submit_prediction(data)
    except EOFError as e:
        break;
