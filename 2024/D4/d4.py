import re
from pathlib import Path


# Get input file
input_file = Path(__file__).with_name('test.txt')

# Parse input into a list for each line
input_lines = [x.strip('\n') for x in open(input_file).readlines()]

# Define axis
x_axis = max(len(line) for line in input_lines)
y_axis = len(input_lines)

# Take a list strings, then append the reverse of all those strings to the original list
def mirror_strings(string_list):
    return string_list + [string[::-1] for string in string_list]


# Create list of diagonal lines
def diagonal_lines(string_list, start_direction):
    y_len = len(string_list)
    string_list_copy = string_list.copy()

    if start_direction == 'south':
        for y in range(y_len-1, -1, -1):
            # Start by creating the first letter for each item in the list
            if y == y_len-1: 
                diagonals = [string[0] for string in string_list_copy] 
                # Remove used elements from the string list by slicing the string
                for i, string in enumerate(string_list_copy):
                    string_list_copy[i] = string_list_copy[i][1:]
                # Add the last row while removing it from the string list
                diagonals += list(string_list_copy.pop(y))
            else:
                # Create the new line to add into diagonals, then remove those
                new_diag = [string[0] for string in string_list_copy]
                for i, string in enumerate(string_list_copy):
                    string_list_copy[i] = string_list_copy[i][1:]
                new_diag += list(string_list_copy.pop(y))
                # Dynamic start/end positions
                diag_start = y_len-1-y
                diag_end = len(diagonals)-diag_start
                # Add a letter for each instance
                x=0
                for i in range(diag_start, diag_end):
                    diagonals[i] += new_diag[x]
                    x += 1
        return diagonals
    
    elif start_direction == 'north': #Everything here is nearly the same as above
        for y in range(0, y_len):
            if y == 0: 
                diagonals = list(string_list_copy.pop(0))
                diagonals += [string[y_len-1] for string in string_list_copy] 
                for i, string in enumerate(string_list_copy):
                    string_list_copy[i] = string_list_copy[i][:y_len-1]
            else:
                new_diag = list(string_list_copy.pop(0))
                new_diag += [string[y_len-1-y] for string in string_list_copy]
                for i, string in enumerate(string_list_copy):
                    string_list_copy[i] = string_list_copy[i][:y_len-1]
                diag_start = 0+y
                diag_end = len(diagonals)-diag_start
                x=0
                for i in range(diag_start, diag_end):
                    diagonals[i] += new_diag[x]
                    x += 1
        return diagonals   
    else:
        raise ValueError("Invalid start direction, use 'north' or 'south'") 


# Make Strings for each direction including its reverse, named using cardinal directions
w_e = mirror_strings(input_lines)
n_s = mirror_strings([''.join(y[x] for y in input_lines) for x in range(x_axis)])
nw_se = mirror_strings(diagonal_lines(input_lines, 'north'))
sw_ne = mirror_strings(diagonal_lines(input_lines, 'south'))


def part_one():
    all_directions = [w_e, n_s, nw_se, sw_ne]
    xmas_count = 0
    for dir in all_directions:
        for string in dir:
            xmas_count += len(re.findall('XMAS|SAMX', string))
    return xmas_count


def part_two():
    return


def main():
    print(f'The answer to part one is {part_one()}.')
    print(f'The answer to part two is {part_two()}.')
    return


if __name__ == '__main__':
    main()
