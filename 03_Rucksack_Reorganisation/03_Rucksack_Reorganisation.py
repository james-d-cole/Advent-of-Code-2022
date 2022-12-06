# Import required modules
import sys

# Read source file
with open(sys.argv[1]) as source_file:
    items = [ x.rstrip('\n') for x in source_file]

# Set up output list
output = []

# Process each item separately
for item in items:
    compartment_1 = [x for x in item[0:int(len(item)/2)]]
    compartment_2 = [x for x in item[int(len(item)/2)::]]
    output.append([x for x in compartment_1 if x in compartment_2][0])

# Convert output to values
value_output = [ord(x)-38 if x.isupper() else ord(x)-96 for x in output]

# Substitute input for scores
print(f"Question 1 answer: {sum(value_output)}")

# Set up output list for question 2
output = []

# Split into chunks of 3 and find overlap, add it to the output list
counter = 0
while counter != len(items):
    output.append([y for y in items[counter+2] if y in [x for x in items[counter] if x in items[counter+1]]][0])
    counter += 3

# Convert output to values
value_output = [ord(x)-38 if x.isupper() else ord(x)-96 for x in output]

# Substitute input for scores
print(f"Question 2 answer: {sum(value_output)}")