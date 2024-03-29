input_file = 'input.txt'
command_list = [str(x.strip('\n')) for x in open(input_file).readlines()]
horizontal_position = 0
depth = 0


def multiple_pos_by_depth():
    process_commands()
    global horizontal_position
    global depth
    return horizontal_position * depth


def process_commands():
    for command in command_list:
        if command[0] == 'f':
            mod_horizontal_position(int(command[-1]))
        if command[0] == 'd':
            mod_depth(int(command[-1]))
        if command[0] == 'u':
            mod_depth(- int(command[-1]))
    return


def mod_horizontal_position(count):
    global horizontal_position
    horizontal_position += count
    return


def mod_depth(count):
    global depth
    depth += count
    return


print(f'The product of horizontal position by final depth is {multiple_pos_by_depth()}.')
