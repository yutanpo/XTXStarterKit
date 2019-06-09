#!/bin/bash 

function printUsage() {
    echo "---------------------------------------------------------------------------------------------------------------------"
    echo "Usage: Should run in the /python directory. Please do not move this file!"
    echo "$ ./run_tester_python.sh"
    echo "This script will ensure that all required components for the model tester are present and in the correct directories."
    echo "Additionally, the script will run the model tester on your Python submissions."
    echo "It is HIGHLY recommended to run this script and fix any errors prior to submitting your code."
    echo "---------------------------------------------------------------------------------------------------------------------"
    echo ""
}

function printExpectedFolderStructure() {
    echo "|--README.md"
    echo "|-- python"
    echo "   |-- core.py"
    echo "   |-- requirements.txt"
    echo "   |-- run_tester_python.sh"
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
    if [ ! -f ./submission.py ]; then
        >&2 echo "[ERROR] submission.py file not found at expected location."
        >&2 echo "[ERROR] Please, refer to the structure below:"
        echo ""
        printExpectedFolderStructure
        exit 1
    else
        echo "[SUCCESS] submission.py found!"
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

function checkCoreFile() {
    if [ ! -f ./core.py ]; then
        >&2 echo "[ERROR] core.py file not found at expected location."
        >&2 echo "[ERROR] Please, refer to the structure below:"
        echo ""
        printExpectedFolderStructure
        exit 1
    else
        echo "[SUCCESS] core.py  found!"
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
    checkCoreFile
    echo ""
    echo "-----------------------------------"
    echo "Finished Running Folder Validation."
    echo "-----------------------------------"
}

function runModelTester() {
    python3 ../src/model_tester.py
}

function main() {
    printUsage
    folderValidation
    runModelTester
}

main
