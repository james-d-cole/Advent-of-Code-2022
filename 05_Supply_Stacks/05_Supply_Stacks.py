# Import required modules
import sys

# Read source file
with open(sys.argv[1]) as source_file:
    items = [x.rstrip('\n') for x in source_file]

# Create the starting crate map
crate_map = items[0:items.index('')-1][::-1]
crate_map = [[item[i:i+4].strip() for i in range(0, len(crate_map[0]), 4)] for item in crate_map]

# Create an empty list to flip the crate map
flipped_map = [[[] for i in range(len(crate_map))] for i in range(len(crate_map[0]))]

# Flip the map around
for i in range(len(flipped_map)):
    for x in range(len(flipped_map[i])):
        flipped_map[i][x] = crate_map[x][i]

# Filter out None value
flipped_map = [list(filter(None,x)) for x in flipped_map]
flipped_map_2 = [list(filter(None,x)) for x in flipped_map]

# Get the instructions
instructions = [x.replace("move ", "").replace("from ", "").replace("to ", "").split(" ") for x in items[items.index('')+1::]]

# Iterate through instructions
for instruction in instructions:
    for i in range(int(instruction[0])):
        popped_item = flipped_map[int(instruction[1])-1].pop()
        flipped_map[int(instruction[2])-1].append(popped_item)

# Answer string
output = ''.join([x[-1] for x in flipped_map])
output = output.replace("[","").replace("]","")

# Print answer
print(f"Answer for question 1: {output}")

# Iterate through instructions for part 2
for instruction in instructions:
    # Extract info from instruction
    no_to_move = int(instruction[0])
    move_from = int(instruction[1])-1
    move_to = int(instruction[2])-1

    # Move the crates
    crates_to_move = flipped_map_2[move_from][-no_to_move:]
    flipped_map_2[move_from] = flipped_map_2[move_from][0:-no_to_move]
    flipped_map_2[move_to].extend(crates_to_move)

# Answer string
output = ''.join([x[-1] for x in flipped_map_2])
output = output.replace("[","").replace("]","")

# Print answer
print(f"Answer for question 2: {output}")
