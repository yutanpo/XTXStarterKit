import subprocess
import sys, os
import time

p = subprocess.Popen(["Rscript", "submission.r"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#p = subprocess.Popen(["python3", "test.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)


def follow(the_process):
    while(True):
        line = the_process.stdout.readline()
        yield line

output = follow(p)

while(True):
    # Read data
    # 
    # get_next_data_raw() or get_next_data_as_list() or get_next_data_as_numpy_array() 
    # MUST be used to read the next row of data
    # NOTE: you can only use one of (get_next_data_raw, get_next_data_as_list, get_next_data_as_numpy_array)
    # to get the row of data, please refer to the `OVERVIEW OF DATA` section above

    # data = self.get_next_data_as_list()
    # data = self.get_next_data_as_numpy_array()
    #print("before read data", file=sys.stderr, flush=True)
    #time.sleep(1)
    data = input()
    
    #print(data, file=sys.stderr, flush=True)
    
    data = data + '\n'
    #print(data.encode(), file=sys.stderr, flush=True)
    p.stdin.write(data.encode())
    p.stdin.flush()

    print(output.__next__().decode("utf-8"), end="")
    #print(str(1))
    sys.stdout.flush()
    #print("after print", file=sys.stderr, flush=True)
