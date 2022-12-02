# Import required modules
import sys

# Read source file
with open(sys.argv[1]) as source_file:
    items = [ x.rstrip('\n') for x in source_file]

# Create score dictionary
scores = {'A X':4, 'A Y':8, 'A Z':3, 
          'B X':1, 'B Y':5, 'B Z':9, 
          'C X':7, 'C Y':2, 'C Z':6}

# Substitute input for scores
print(f"Question 1 answer: {sum([scores[x] for x in items])}")

# Create updated score dictionary
updated_scores = {'A X':3, 'A Y':4, 'A Z':8, 
                  'B X':1, 'B Y':5, 'B Z':9, 
                  'C X':2, 'C Y':6, 'C Z':7}

# Substitute input for scores
print(f"Question 2 answer: {sum([updated_scores[x] for x in items])}")
