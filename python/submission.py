import subprocess
from core import Submission

# PYTHON submission
#
# Implement your model below
#
###################################################### OVERVIEW ######################################################
# 
# 1. Use get_next_data_raw() OR get_next_data_list() OR get_next_data_numpy_array() to recieve the next row of data
# 2. Use predict method to write your prediction logic, and return a float representing your prediction
# 4. Submit prediction using self.submit_prediction(...)
#
######################################################################################################################
#
################################################## OVERVIEW OF DATA ##################################################
# 
# 1. get_next_data_raw() accepts no input and returns a String representing a row of data extracted from data.csv
#	 Example output: 
# 2. get_next_data_list() accepts no input and returns a List representing a row of data extracted from data.csv, 
# 	 missing data is represented as NaN (math.nan)
#	 Example output: 
# 3. get_next_data_numpy_array() accepts no inputa nd returns a Numpy Array representing a row of data extracted from data.csv, 
# 	 missing data is represented as NaN (math.nan)
#    Example output:
#
######################################################################################################################
#
###################################################### IMPORTANT ######################################################
# 
# 1. You MUST use (get_next_data_raw(), get_next_data_list(), get_next_data_numpy_array() and submit_prediction(pred) 
# 	 below for your submissions to work correctly
# 2. (get_next_data_raw(), get_next_data_list(), get_next_data_numpy_array()) CANNOT be called more then once
# 	 in a row without calling self.submit_prediction(pred).
# 3. In order to debug by printing do NOT call the default method `print(...)`, rather call self.debug_print(...)
#
######################################################################################################################


# class MySubmission is the class that you will need to implement
#    the class contains two methods: 
# 		1. predict, where you will write your prediction logic
#       2. run_submission, a method that will keep fetching the next row of data for every prediction submitted
#          NOTE: this method will not fetch the next row of data, unless a prediction is submitted

class MySubmission(Submission):

	# predict(data) expects data as input and should return a 
	#    float that represents a prediction for the supplied
	#    row of data
	def predict(self, data):
		return 1.0

    # run_submission() will iteratively fetch the next row of data in the format 
    #    specified (get_next_data_raw, get_next_data_list, get_next_data_numpy_array)
    #    for every prediction submitted to self.submit_prediction()
	def run_submission(self):
		self.debug_print("Use this print function for debugging purposes, do NOT use the default `print(...)`")

		while(True):
			# Read data
			# 
			# get_next_data_raw() or get_next_data_list() or get_next_data_numpy_array() 
			# MUST be used to read the next row of data
			# NOTE: you can only use one of (get_next_data_raw, get_next_data_list, get_next_data_numpy_array)
			# to get the row of data, please refer to the `OVERVIEW OF DATA` section above

			# data = self.get_next_data_list()
			# data = self.get_next_data_numpy_array()
			data = self.get_next_data_raw()

			prediction = self.predict(data)

			# submit_prediction(pred) MUST be used submit your 
			# prediction for the current row of data
			self.submit_prediction(prediction)


if __name__ == "__main__":
    MySubmission()
