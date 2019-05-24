import subprocess
from core import Submission

# Python submission
# 
# Implement your model below
# 
# 1. Use get_next_data to receive the next row of data
# 2. Predict the value

class MySubmission(Submission):

    def run_submission(self):
    	# IMPORTANT !!!
		# 
		# 1. You MUST use get_next_data() and submit_prediction(pred) 
		# 	 below for your submissions to work correctly
		#
		# 2. get_next_data() CANNOT be called more then once
		# 	 in a row without calling self.submit_prediction(pred).
        while(True):
            # Read data
		    # 
		    # get_next_data() MUST be used to read the next now of data
            data = self.get_next_data()

            # Guess 1 every time
		    #
		    # submit_prediction(pred) MUST be used submit your 
		    # prediction for the current row of data
            self.submit_prediction(1)


if __name__ == "__main__":
    MySubmission()
