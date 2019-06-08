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
#	 Example output: '1619.5,1620.0,1621.0,,,,,,,,,,,,,1.0,10.0,24.0,,,,,,,,,,,,,1615.0,1614.0,1613.0,1612.0,1611.0,1610.0,1607.0,1606.0,1605.0,1604.0,1603.0,1602.0,1601.5,1601.0,1600.0,7.0,10.0,1.0,10.0,20.0,3.0,20.0,27.0,11.0,14.0,35.0,10.0,1.0,10.0,13.0'
# 2. get_next_data_list() accepts no input and returns a List representing a row of data extracted from data.csv, 
# 	 missing data is represented as NaN (math.nan)
#	 Example output: [1619.5, 1620.0, 1621.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, 10.0, 24.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1615.0, 1614.0, 1613.0, 1612.0, 1611.0, 1610.0, 1607.0, 1606.0, 1605.0, 1604.0, 1603.0, 1602.0, 1601.5, 1601.0, 1600.0, 7.0, 10.0, 1.0, 10.0, 20.0, 3.0, 20.0, 27.0, 11.0, 14.0, 35.0, 10.0, 1.0, 10.0, 13.0]
# 3. get_next_data_numpy_array() accepts no inputa nd returns a Numpy Array representing a row of data extracted from data.csv, 
# 	 missing data is represented as NaN (math.nan)
#    Example output: [1.6195e+03 1.6200e+03 1.6210e+03 nan nan nan nan nan nan nan nan nan nan nan nan 1.0000e+00 1.0000e+01 2.4000e+01 nan nan nan nan nan nan nan nan nan nan nan nan 1.6150e+03 1.6140e+03 1.6130e+03 1.6120e+03 1.6110e+03 1.6100e+03 1.6070e+03 1.6060e+03 1.6050e+03 1.6040e+03 1.6030e+03 1.6020e+03 1.6015e+03 1.6010e+03 1.6000e+03 7.0000e+00 1.0000e+01 1.0000e+00 1.0000e+01 2.0000e+01 3.0000e+00 2.0000e+01 2.7000e+01 1.1000e+01 1.4000e+01 3.5000e+01 1.0000e+01 1.0000e+00 1.0000e+01 1.3000e+01]
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
		self.debug_print("Use the print function `self.debug_print(...)` for debugging purposes, do NOT use the default `print(...)`")

		while(True):
			# Read data
			# 
			# get_next_data_raw() or get_next_data_list() or get_next_data_numpy_array() 
			# MUST be used to read the next row of data
			# NOTE: you can only use one of (get_next_data_raw, get_next_data_list, get_next_data_numpy_array)
			# to get the row of data, please refer to the `OVERVIEW OF DATA` section above

			# data = self.get_next_data_list()
			data = self.get_next_data_numpy_array()
			# data = self.get_next_data_raw()

			self.debug_print(data)

			prediction = self.predict(data)
			# submit_prediction(pred) MUST be used submit your 
			# prediction for the current row of data
			self.submit_prediction(prediction)


if __name__ == "__main__":
    MySubmission()
