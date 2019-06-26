### R

NOTE: we expect you to have Python 3 installed in order to run `run_tester_r.py`. You will not need to make changes to `run_tester_r.py`, it is used to test your submission.

Requirements: Python 3.6 or higher

Also ensure that R is installed on your machine. Installation information can be found [here](https://www.andrewheiss.com/blog/2012/04/17/install-r-rstudio-r-commander-windows-osx/)

We require your system to be able to run `Rscript` commands.

Files that are required for your submission to run successfully such as: models, files that you create must be stored in `r`. 

Place required R packages in the `requirements.txt` file. These packages will be installed on the fly on our submission environment. 

With that being said, our testing script `run_tester_r.py` will NOT install these packages; therefore, please ensure your system has the packages installed in order to test locally. 

## Quickstart (macOS and Linux)

At all phases of the development process it is highly recommended to run `python3 run_tester_r.py` from within the `r` directory.

If your submission is not able to run with `python3 run_tester_r.py` it will NOT run on our platform.

This script will ensure that the submission folder satisfies:

|--README.md \
--|-- r \
-----|-- core.r \
-----|-- requirements.txt \
-----|-- submission.r \
--|-- src \
-----|-- model_tester.py \
-----|-- scorer.py \
--|-- data.csv \

The script `run_tester_r.py` will also run `src/model_tester.py`, and return a score. 

The result & score can be found in the results folder that will be created upon successfully running `python3 run_tester_r.py`.