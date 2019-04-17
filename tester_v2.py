import time
import subprocess

print("Starting...")
def follow(the_process):
    while(True):
        line = the_process.stdout.readline()
        yield line

p = subprocess.Popen(["python3", "sample_v2.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
output = follow(p)

with open('data.csv') as fp:
    while(True):
        print("Looping...")
        line = fp.readline()
        if not line: #EOF
            break;
        p.stdin.write(str.encode(line))
        p.stdin.flush()
        output.__next__()


