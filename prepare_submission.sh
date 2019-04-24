#!/bin/bash

# remove old zipfile
rm -f submission.zip

# zip directory contents (excluding data files)
zip -r submission.zip * -x *.csv
