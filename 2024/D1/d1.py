from pathlib import Path

# Get input file
input_file = Path(__file__).with_name('input.txt')

# Parse input file, making a list by new lines and an imbeded list where the left and right contents are separated
original_pairs = [x.strip('\n').split('   ') for x in open(input_file).readlines()]
# Split left and Right lists into their own objects
left_list = [int(original_pairs[x][0]) for x in range(0, len(original_pairs))]
right_list = [int(original_pairs[x][-1]) for x in range(0, len(original_pairs))]


# Part 1
def part_one():
    total_distance = 0
    # Sort the two lists
    ranked_left_list = left_list.copy()
    ranked_left_list.sort()
    ranked_right_list = right_list.copy()
    ranked_right_list.sort()
    # Compare the distances from each listed item and add it to the total_distance
    for pair in range(0, len(original_pairs)):
        total_distance += abs(ranked_left_list[pair] - ranked_right_list[pair])
    return print(f'The answer to part one is {total_distance}.')


# Part 2
def part_two(): 
    similarity_score = 0
    # Check for occurences of left list items in the right list
    for left_item in left_list:
        mult = 0
        if left_item not in right_list:
            continue
        for right_item in right_list:
            if right_item == left_item:
                mult += 1
        # Multiply the left item by the number of occurences in the right list, add to simularity_score
        similarity_score += left_item * mult
    return print(f'The answer to part two is {similarity_score}.')


# Solve all the problems
def main():
    part_one()
    part_two()
    return


#Run the code
if __name__ == '__main__':
    main()