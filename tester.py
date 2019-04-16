import time
import random
import subprocess


def follow(the_file):
    f = subprocess.Popen(['tail', '-F', the_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while(True):
        line = f.stdout.readline()
        if not line:
            continue
        yield line

with open('data.csv') as fp:
    output = follow('output.txt')
    while(True):
        with open('input.txt', "a+") as wp:
            line = fp.readline()
            if not line: # EOF reached
                break; # TODO: Send token to tell other program to terminate
            wp.write(line)
        output.__next__()
        
