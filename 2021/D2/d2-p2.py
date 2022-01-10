input_file = 'input.txt'
command_list = [str(x.strip('\n')) for x in open(input_file).readlines()]
horizontal_position = 0
depth = 0
aim = 0


def multiple_pos_by_depth():
    process_commands()
    global horizontal_position
    global depth
    return horizontal_position * depth


def process_commands():
    for command in command_list:
        if command[0] == 'd':
            mod_aim(int(command[-1]))
        if command[0] == 'u':
            mod_aim(- int(command[-1]))
        if command[0] == 'f':
            move_forward(int(command[-1]))
    return


def mod_aim(count):
    global aim
    aim += count
    return


def move_forward(count):
    global aim
    global depth
    global horizontal_position
    horizontal_position += count
    depth += aim * count
    return


print(f'The product of my final depth and horizontal position is {multiple_pos_by_depth()}.')
