"""
This file is used to test your model.

CHANGES TO THIS FILE ARE NOT SUBMITTED.
"""

import time
import subprocess
import sys

# Change these paths to point to your local machine
RESULT_LOCATION = '/app/data/result.txt'
DATASET_LOCATION = 'data.csv'
SCORE_LOCATION = '/app/data/score.txt'

argc = len(sys.argv)

def follow(the_process):
    while(True):
        line = the_process.stdout.readline()
        yield line

p = subprocess.Popen(["python3", "sample.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) \
    if not(argc > 1 and argv[1] == "r") else \
    subprocess.Popen(["r", "-f", "sample.r", "--slave"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

output = follow(p)

with open(DATASET_LOCATION) as data_file, open(RESULT_LOCATION, 'a+') as result_file:
    # Skip header
    header = data_file.readline()
    print(header)

    while(True):
        data_row = data_file.readline()
        if not data_row: # EOF
            break
        
        p.stdin.write(str.encode(data_row))
        p.stdin.flush()

        print(p.stderr.read())

        output.__next__().decode("utf-8")

# Score submission
p = subprocess.run(["python3", "scorer.py", RESULT_LOCATION, DATASET_LOCATION, SCORE_LOCATION])
