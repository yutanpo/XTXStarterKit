#!/usr/bin/Rscript

# R Starter Kit
# 
# Implement your model below
# 
# 1. Use get_next_data to receive your data
# 2. Predict the value

input <- file('stdin')
open(input, 'rb')

# Receives a line of data from standard input
#
# Standard input is fed into your algorithm
# ONLY after a prediction for the previous
# row of data is received.
get_next_data <- function() {
  readLines(input, n=1)
}

# Prints prediction standard out
#
# Use this function for submitting
# your actual prediction
submit_prediction <- function(pred) {
  write(pred, stdout()) 
}

# Prints to standard error
# 
# Use this for development / debugging
# Output sent to standard error will not
# be scored.
eprint <- function(msg) {
  write(msg, stderr())
}

### IMPLEMENT YOUR ALGORITHM BELOW ###
# 
# This sample algorithm naively sends 
# 1 as the prediction for every line
# of data

while (TRUE) {
  tryCatch({
    
    # Read data
    data <- get_next_data()

    # Guess 1 every time
    submit_prediction(1)

  }, error=function(e){})
} 
