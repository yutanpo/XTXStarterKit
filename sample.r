library(subprocess)

input<-file('stdin', 'r')

get_next_data <- function() {
  readLines(input, n=1)
}

submit_prediction <- function(pred) {
  cat(pred + "\n")
}

### YOUR CODE BELOW

### Basic sample algorithm
while (TRUE) {
  ### Read data
  data <- get_next_data()
  
  ### Guess 3 every time
  submit_prediction(3) 
}
