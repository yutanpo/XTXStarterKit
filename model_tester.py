"""
This file is used to test your model.

CHANGES TO THIS FILE ARE NOT SUBMITTED.
"""

import time
import subprocess
import sys
import multiprocessing

# Change these paths to point to your local machine
RESULT_LOCATION = '/app/data/result.txt'
DATASET_LOCATION = 'data.csv'
SCORE_LOCATION = '/app/data/score.txt'
INCLUDE_Y_VALUE = False
argc = len(sys.argv)

def log_pipe(pipe):
    for line in iter(pipe.stderr.readline, b''):
        print(line)

def follow(the_process):
    while(True):
        line = the_process.stdout.readline()
        yield line

p = subprocess.Popen(["python3", "sample.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) \
    if not(argc > 1 and argv[1] == "r") else \
    subprocess.Popen(["r", "-f", "sample.r", "--slave"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

stderr_logger_thread = multiprocessing.Process(target=log_pipe, args=(p,))
stderr_logger_thread.start()

output = follow(p)

with open(DATASET_LOCATION) as data_file, open(RESULT_LOCATION, 'a+') as result_file:
    # Skip header
    header = data_file.readline()
    print(header)

    while(True):
        data_row = data_file.readline()
        if not data_row: # EOF
            break
            
        if not INCLUDE_Y_VALUE:
            data_row = ','.join(data_row.split(',')[:-1]) + '\n'

        p.stdin.write(str.encode(data_row))
        p.stdin.flush()
        result_file.write(output.__next__().decode("utf-8"))

stderr_logger_thread.terminate()

# Score submission
p = subprocess.run(["python3", "scorer.py", RESULT_LOCATION, DATASET_LOCATION, SCORE_LOCATION])

