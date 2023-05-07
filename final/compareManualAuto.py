# compares the manual ground truth labels to GPT generated labels of matches to question

import argparse
import json

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Compare two JSON files of arrays.')

# Add two arguments for the filenames
parser.add_argument('file1', type=str, help='the name of the first file')
parser.add_argument('file2', type=str, help='the name of the second file')

# Parse the arguments
args = parser.parse_args()

path = "data/labels/"

# Read in the two files
with open(path + args.file1, 'r') as f1, open(path + args.file2, 'r') as f2:
    data1 = json.load(f1)
    data2 = json.load(f2)

# Compare the arrays and count the matches and differences
matches = 0
differences = 0
total = 0
for key in data1:
    if key in data2:
        array1 = data1[key]
        array2 = data2[key]
        length = min(len(array1), len(array2))
        for i in range(length):
            if array1[i] == array2[i]:
                matches += 1
            else:
                differences += 1
            total += 1

# Calculate the accuracy level
accuracy = matches / total * 100

# Print the results
print(f"Number of matches: {matches}")
print(f"Number of differences: {differences}")
print(f"Accuracy level: {accuracy:.2f}%")
