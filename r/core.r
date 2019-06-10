# Receives a line of data from standard input
#
# Standard input is fed into your algorithm
# ONLY after a prediction for the previous
# row of data is received.
get_next_data_raw <- function() {
  readLines(input, n=1)
}

get_next_data_as_list <- function() {
  raw_data <- readLines(input, n=1)
  strsplit(raw_data, ',')[[1]]
}

get_next_data_as_dataframe <- function() {
  raw_data <- readLines(input, n=1)
  read.csv(text=raw_data, sep=',', header=FALSE)
}

get_next_data_as_matrix <- function() {
  raw_data <- readLines(input, n=1)
  data_frame <- read.csv(text=raw_data, sep=',', header=FALSE)
  return(as.matrix(data_frame))
}

# Prints prediction standard out
#
# Use this function for submitting
# your actual prediction
submit_prediction <- function(pred) {
  enable_print()
  write(pred, stdout()) 
  disable_print()
}

# Prints to standard error
# 
# Use this for development / debugging
# Output sent to standard error will not
# be scored.
debug_print <- function(msg) {
  message(paste0(capture.output(msg), collapse = "\n"))
}

enable_print <- function() {
  sink()
}

disable_print <- function() {
  sink("/dev/null")
}

init <- function() {
  disable_print()
}
