# Import required modules
import sys

# Main program
if __name__ == "__main__":

    # Check 2 args are present
    if len(sys.argv) != 3:
        print("Usage: scripts/1_sonar_sweep.py <input file> <window size>", file=sys.stderr)
        sys.exit(-1)

    # Wrap in a try except block for error handling
    try:

        # Define item comparison function
        def comparison(list):
            count = 0
            for i in range(len(list)-1):
                if list[i+1] > list[i]:
                    count += 1
            return(count)

        # Read source file
        with open(sys.argv[1]) as source_file:
            items = [ int(x.rstrip('\n')) for x in source_file]

        # Create a list containing an <x> measurement window
        windowed_list = []
        window_size = int(sys.argv[2])
        for i in range(len(items)-len(items)%window_size):
            windowed_list.append(sum(items[i:i+window_size]))

        # Print result to part 1
        print(f"Part 1 answer (no windows): {comparison(items)}")

        # Print result to part 2
        print(f"Part 2 answer: ({window_size} item measurement window) {comparison(windowed_list)}")

    except:
        print("Error: please check the input file path is correct, and window size is an integer", file=sys.stderr)
        sys.exit(-1)
