import time

### Changes you make to this file will not persist to our testing servers

RESULT_LOCATION = 'output.txt'
DATASET_LOCATION = 'data.csv'

err2_tally = 0
y2_tally = 0

with open(DATASET_LOCATION, 'r') as dp:
    with open(RESULT_LOCATION, 'r') as sp:
        i = 0
        while(True):
            line = dp.readline()
            if not line:
                break;
            if i == 0:
                i += 1
                continue; # don't read first line of data because it contains headers
            y_true = float(line.split(',')[-1][:-1])

            guess_line = sp.readline()[:-1] 
            y_guess = float(guess_line)
            
            err2_tally += (y_true - y_guess) ** 2
            y2_tally += y_true ** 2

r2 = 1 - err2_tally / y2_tally

print("You achieved an r2 value of :{}".format(r2))
