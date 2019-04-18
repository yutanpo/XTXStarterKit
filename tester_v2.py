import time
import subprocess

def follow(the_process):
    while(True):
        line = the_process.stdout.readline()
        yield line

p = subprocess.Popen(["python3", "sample_v2.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
output = follow(p)

with open('data.csv') as fp:
    with open('/app/data/result.txt', 'a+') as wp:
        while(True):
            line = fp.readline()
            if not line: #EOF
                break;
            p.stdin.write(str.encode(line))
            p.stdin.flush()
            wp.write(output.__next__().decode("utf-8"))


