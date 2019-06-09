#!/usr/bin/Rscript
source("core.r")

# R submission
#
# Implement your model below
#
###################################################### OVERVIEW ######################################################
# 
# 1. Use get_next_data_raw() OR get_next_data_as_list() OR get_next_data_as_dataframe() OR get_next_data_as_matrix() to receive a row of data
# 2. Use predict method to write your predicition logic, and return a float representing your prediction
# 3. Submit your prediction using submit_prediction
#
######################################################################################################################
#
################################################## OVERVIEW OF DATA ##################################################
# 
#
#
######################################################################################################################
#
###################################################### IMPORTANT ######################################################
# 
#
#
#
######################################################################################################################


input <- file('stdin')
open(input, 'rb')

init()

### IMPLEMENT YOUR ALGORITHM BELOW ###
# 
# This sample algorithm naively sends 
# 1 as the prediction for every line
# of data
#
# IMPORTANT !!!
# 
# 1. You MUST use get_next_data() and submit_prediction(pred) 
# 	 below for your submissions to work correctly
#
# 2. get_next_data() CANNOT be called more then once
# 	 in a row without calling self.submit_prediction(pred).
#
# 3. In order to debug by printing do NOT call the default method `print(...)`, rather call debug_print(...)

get_prediction <- function(data) {
  return(1)
}

while (TRUE) {
  tryCatch({
    
    # Read data
    # 
    # get_next_data() MUST be used to read the next now of data
   
    #data <- get_next_data_as_dataframe()
    #data <- get_next_data_as_list()
    #data <- get_next_data_as_matrix()
    data <- get_next_data_raw()

    # data <- get_next_data_raw()
    prediction <- get_prediction(data)

    # Guess 1 every time
    #
    # submit_prediction(pred) MUST be used submit your 
    # prediction for the current row of data

    submit_prediction(prediction)

  }, error=function(e){quit()})
} 
