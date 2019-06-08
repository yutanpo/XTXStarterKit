import sys
import math
import numpy
import os

def block_print():
    sys.stdout = open(os.devnull, 'w')

def enable_print():
    sys.stdout = sys.__stdout__

class Submission():
    def __init__(self):
        try:
            block_print()
            self.run_submission()
        except EOFError as e:
            pass

    def run_submission(self):
        raise NotImplementedError("Please implement run_submission in your " +
                "submission class")

    def get_next_data_raw(self):
        """
        Reads input from standard input

        Use this to supply your model with input
        Input will not be supplied until output is 
        generated for the previous input
        """
        return input()
        
    def get_next_data_list(self):
        """
        Reads input from standard input and stores row in a 
        list where missing values are represented as NaN

        Use this to supply your model with input
        Input will not be supplied until output is 
        generated for the previous input
        """
        raw_data_list = input().split(",")

        # replace empty spots with NaN
        data_list = []
        for order in data_list:
            if not order:
                data_list.append(math.nan)
            else:
                data_list.append(float(order))
        
        return data_list
    
    def get_next_data_numpy_array(self):
        """
        Reads input from standard input and stores row in a
        numpy array where missing values are represented as NaN

        Use this to supply your model with input
        Input will not be supplied until output is 
        generated for the previous input
        """
        return np.array(get_next_data_list)
    
    def submit_prediction(self, prediction):
        """
        Submits your prediction to standard output
        """
        enable_print()
        print(str(prediction))
        block_print()

    def debug_print(self, msg):
        """
        Prints to standard error

        Use this to debug / develop. 
        This output will not be scored
        """
        print(msg, file=sys.stderr)


