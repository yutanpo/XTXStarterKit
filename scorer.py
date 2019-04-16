import time

err2_tally = 0
y2_tally = 0

last_y = 0.0
with open('data.csv', 'r') as dp:
    with open('output.txt', 'r') as sp:
        i = 0
        while(True):
            line = dp.readline()
            if not line:
                break;
            if i == 0:
                i += 1
                continue;
            y_true = float(line.split(',')[-1][:-1])
            guess_line = sp.readline()[:-1]
            y_guess = last_y
            last_y = y_true
            #y_guess = float(guess_line)
            err2_tally += (y_true - y_guess) ** 2
            y2_tally += y_true ** 2

r2 = 1 - err2_tally / y2_tally

print(r2)
