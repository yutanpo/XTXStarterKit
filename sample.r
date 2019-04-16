library(subprocess)

handle <- spawn_process('r_script.sh')

get_next_data <- function() {
  process_read(handle, timeout = 10000)
}

submit_prediction <- function(pred) {
  write(pred, file="output.txt", append=TRUE)
}

### YOUR CODE BELOW

### Basic sample algorithm
while (TRUE) {
  ### Read data
  data <- get_next_data()
  
  ### Guess 3 every time
  submit_prediction(3) 
}
