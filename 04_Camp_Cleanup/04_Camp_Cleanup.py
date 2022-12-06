# Import required modules
import sys

# Read source file
with open(sys.argv[1]) as source_file:
    items = [x.rstrip('\n') for x in source_file]

# Split into nested list
items_split = [x.split(",") for x in items]

# Iterate through list and calculate result for each pair
counter = 0
for item in items_split:
    item_split = [x.split("-") for x in item]
    if int(item_split[0][0]) >= int(item_split[1][0]) and int(item_split[0][1]) <= int(item_split[1][1]):
        counter += 1
    elif int(item_split[1][0]) >= int(item_split[0][0]) and int(item_split[1][1]) <= int(item_split[0][1]):
        counter += 1

# Print answer
print(f"Question 1 answer: {counter}")

# Iterate through list and calculate result for question 2
counter = 0
for item in items_split:
    item_split = [x.split("-") for x in item]
    if int(item_split[1][0]) <= int(item_split[0][0]) <= int(item_split[1][1]):
        counter += 1
    elif int(item_split[1][0]) <= int(item_split[0][1]) <= int(item_split[1][1]):
        counter += 1
    elif int(item_split[0][0]) <= int(item_split[1][1]) <= int(item_split[0][1]):
        counter += 1
    elif int(item_split[0][0]) <= int(item_split[1][0]) <= int(item_split[0][1]):
        counter += 1

# Print answer
print(f"Question 2 answer: {counter}")