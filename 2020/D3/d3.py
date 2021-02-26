input_file = 'input.txt'
slope_list = ['1,1', '3,1', '5,1', '7,1', '1,2']


def create_input_list():
    input_list = list(open(input_file).readlines())  # Create a list with each line
    for index, x in enumerate(input_list):  # Clean the \n out of every entry
        input_list[index] = x.strip('\n')
    return input_list


def find_dimensions(input_list, x_rule):
    y_max = len(input_list)
    line_len = len(input_list[0])
    x_max = y_max * x_rule + (line_len - ((y_max * x_rule) % line_len))
    # Adds to y_max * x_rule to make it evenly divisible by line_len
    x_multiplier = x_max / line_len
    return x_max, y_max, x_multiplier


def expand_lines(input_list, x_multiplier):
    full_map = list((k * int(x_multiplier)) for k in input_list)
    return full_map


def find_slope(slope):
    slope_split = list(slope.split(','))
    return int(slope_split[0]), int(slope_split[-1])


def count_trees(slope):
    tree_count = 0
    x_pos = 0
    x_rule, y_rule = find_slope(slope)
    input_list = create_input_list()
    x_max, y_max, x_multiplier = find_dimensions(input_list, x_rule)
    full_map = expand_lines(input_list, x_multiplier)
    for y in range(0, y_max, y_rule):
        y_pos = full_map[y]
        if y_pos[x_pos] == '#':
            tree_count += 1
        x_pos += x_rule
    return tree_count


def choose_slope(part):
    if part == 'part1':
        return count_trees(slope_list[1])
    if part == 'part2':
        total_trees = 1
        for x in slope_list:
            total_trees = count_trees(x) * total_trees
        return total_trees


print(f"In Part 1 you would encounter {choose_slope('part1')} trees.")
print(f"The answer to part 2 is {choose_slope('part2')}.")
