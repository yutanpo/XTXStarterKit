#!/bin/bash 

function printUsage() {
    echo "---------------------------------------------------------------------------------------------------------------------"
    echo "Usage: Should run in the /r directory. Please do not move this file!"
    echo "$ ./test_submission.sh"
    echo "This script will ensure that all required components for the model tester are present and in the correct directories."
    echo "Additionally, the script will run the model tester on your R submissions."
    echo "It is HIGHLY recommended to run this script and fix any errors prior to submitting your code."
    echo "---------------------------------------------------------------------------------------------------------------------"
    echo ""
}

function printExpectedFolderStructure() {
    echo "|--README.md"
    echo "|-- python"
    echo "   |-- core.py"
    echo "   |-- requirements.txt"
    echo "   |-- test_submission.sh"
    echo "   |-- submission.py"
    echo "|-- r"
    echo "   |-- requirements.txt"
    echo "   |-- submission.r"
    echo "|-- src"
    echo "   |-- model_tester.py"
    echo "   |-- scorer.py"
    echo "|-- data.csv"
}

function checkDataFilePresent() {
    if [ ! -f ../data.csv ]; then
        >&2 echo "[ERROR] data.csv file not found at expected location."
        >&2 echo "[ERROR] Please, refer to the structure below:"
        echo ""
        printExpectedFolderStructure
        exit 1
    else
        echo "[SUCCESS] data.csv found!"
    fi
}

function checkSubmissionFile() {
    if [ ! -f ./submission.r ]; then
        >&2 echo "[ERROR] submission.r file not found at expected location."
        >&2 echo "[ERROR] Please, refer to the structure below:"
        echo ""
        printExpectedFolderStructure
        exit 1
    else
        echo "[SUCCESS] submission.r found!"
    fi
}

function checkModelTester() {
    if [ ! -f ../src/model_tester.py ]; then
        >&2 echo "[ERROR] model_tester.py file not found at expected location."
        >&2 echo "[ERROR] Please, refer to the structure below:"
        echo ""
        printExpectedFolderStructure
        exit 1
    else
        echo "[SUCCESS] model_tester.py found!"
    fi
}

function checkScorerFile() {
    if [ ! -f ../src/scorer.py ]; then
        >&2 echo "[ERROR] scorer.py file not found at expected location."
        >&2 echo "[ERROR] Please, refer to the structure below:"
        echo ""
        printExpectedFolderStructure
        exit 1
    else
        echo "[SUCCESS] scorer.py found!"
    fi
}

function checkRequirementsFile() {
    if [ ! -f ./requirements.txt ]; then
        >&2 echo "[ERROR] requirements.txt file not found at expected location."
        >&2 echo "[ERROR] Please, refer to the structure below:"
        echo ""
        printExpectedFolderStructure
        exit 1
    else
        echo "[SUCCESS] requirements.txt found!"
    fi
}

function folderValidation() {
    echo "----------------------------"
    echo "Starting Folder Validation."
    echo "----------------------------"
    echo ""
    checkDataFilePresent
    checkSubmissionFile
    checkModelTester
    checkScorerFile
    checkRequirementsFile
    echo ""
    echo "-----------------------------------"
    echo "Finished Running Folder Validation."
    echo "-----------------------------------"
}

function runModelTester() {
    python3 ../src/model_tester.py r
}

function main() {
    printUsage
    folderValidation
    runModelTester
}

main
