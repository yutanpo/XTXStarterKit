import time
import subprocess
import sys
### Changes you make to this file will not persist on our testing servers
RESULT_LOCATION = '/app/data/result.txt'
DATASET_LOCATION = 'data.csv'
SCORE_LOCATION = '/app/data/score.txt'
INCLUDE_Y_VALUE = False
argc = len(sys.argv)

def follow(the_process):
    while(True):
        line = the_process.stdout.readline()
        yield line

p = subprocess.Popen(["python3", "sample.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE) \
    if not(argc > 1 and argv[1] == "r") else \
    subprocess.Popen(["r", "-f", "sample.r", "--slave"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

output = follow(p)

with open(DATASET_LOCATION) as fp:
    with open(RESULT_LOCATION, 'a+') as wp:
        while(True):
            line = fp.readline()
            if not line: #EOF
                break

            if not INCLUDE_Y_VALUE:
                line = ','.join(line.split(',')[:-1]) + '\n'
            p.stdin.write(str.encode(line))
            p.stdin.flush()
            wp.write(output.__next__().decode("utf-8"))

# Score submission
p = subprocess.run(["python3", "scorer.py", RESULT_LOCATION, DATASET_LOCATION, SCORE_LOCATION])
