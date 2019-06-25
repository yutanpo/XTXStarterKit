"""
This file is used to test your model.
CHANGES TO THIS FILE ARE NOT SUBMITTED.
"""

import time, subprocess, sys, multiprocessing, os, platform, socket

# Change these paths to point to your local machine
cwd = os.path.split(os.getcwd())[0]
RESULT_LOCATION = os.path.join(cwd, 'results/result.txt')
DATASET_LOCATION = os.path.join(cwd, 'data.csv')
FULL_DATASET_LOCATION = os.path.join(cwd, 'data_training.csv')
SCORE_LOCATION = os.path.join(cwd, 'results/score.txt')

INCLUDE_Y_VALUE = False
lines_processed = 0
argc = len(sys.argv)


def log_pipe(pipe):
    try:
        for line in iter(pipe.stderr.readline, b''):
            print(line.decode('utf-8'))
    except AttributeError as e:
        pass

def follow(the_process):
    while(True):
        line = the_process.stdout.readline()
        yield line

def __create_dir(filepath):
    if not os.path.exists(os.path.dirname(filepath)):
        try:
            os.makedirs(os.path.dirname(filepath))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

__create_dir(RESULT_LOCATION)
__create_dir(SCORE_LOCATION)


if not os.path.isfile(FULL_DATASET_LOCATION):
    print(f"Could not find full training dataset, please see README.md to download the entire dataset.")

if not os.path.isfile(DATASET_LOCATION):
    print(f"Cannot find dataset at {DATASET_LOCATION}, please move dataset \
            here or specify dataset path")


if platform.system() == "Windows":
    python_tag = "py"
else:
    python_tag = "python3"

p = subprocess.Popen([python_tag, "submission.py"], stdin=subprocess.PIPE,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE) \
    if not(argc > 1 and sys.argv[1] == "r") else \
    subprocess.Popen(["Rscript", "submission.r"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)

output = follow(p)

with open(DATASET_LOCATION) as data_file, open(RESULT_LOCATION, 'w') as result_file:
    # Skip header
    header = data_file.readline()

    while(True):
        data_row = data_file.readline()
        if not data_row: # EOF
            break
        
        lines_processed += 1

        if not INCLUDE_Y_VALUE:
            data_row = ','.join(data_row.split(',')[:-1]) + '\n'

        try:
            p.stdin.write(str.encode(data_row))
            p.stdin.flush()
        except socket.error as e:
            print(str(e))
            print(p.stderr.read().decode("utf-8"))
            raise

        if lines_processed % 10000 == 0:
            print(f"Submitted a prediction for {lines_processed} data rows.")
        
        pred = output.__next__().decode("utf-8")
       
        if platform.system() == "Windows":
            result_file.write(pred[:-1])
        else:
            result_file.write(pred)

# Score submission
p = subprocess.run([python_tag, "../src/scorer.py", RESULT_LOCATION, DATASET_LOCATION, SCORE_LOCATION])
