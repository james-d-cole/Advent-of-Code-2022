# Import required modules
import sys

# Read source file
with open(sys.argv[1]) as source_file:
    items = [ x.rstrip('\n') for x in source_file]

# Create output list
output_list = []
curr_count = 0

# Add elements until you hit a blank
for item in items:
    if item == "":
        output_list.append(curr_count)
        curr_count = 0
    else:
        curr_count += int(item)#

# Sort the list for question 2
output_list.sort()

# Print answers
print(f"Answer to question 1: {max(output_list)}")
print(f"Answer to question 2: {sum(output_list[-3::])}")