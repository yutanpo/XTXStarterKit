import time
import subprocess

### Changes you make to this file will not persist on our testing servers

RESULT_LOCATION = '/app/data/result.txt'
DATASET_LOCATION = 'data.csv'

def follow(the_process):
    while(True):
        line = the_process.stdout.readline()
        yield line

p = subprocess.Popen(["python3", "sample_v2.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#p = subprocess.Popen(["r", "-f", "sample.r", "--slave"], stdin=subprocess.PIPE, stdout=subprocess.PIPE) #for R programs
output = follow(p)

with open(DATASET_LOCATION) as fp:
    with open(RESULT_LOCATION, 'a+') as wp:
        while(True):
            line = fp.readline()
            if not line: #EOF
                break;
            p.stdin.write(str.encode(line))
            p.stdin.flush()
            wp.write(output.__next__().decode("utf-8"))


