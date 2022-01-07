input_file = 'test.txt'
command_list = [str(x) for x in open(input_file).readlines()]
horizontal_position = 0
depth = 0


def multiple_pos_by_depth():
    process_commands()
    global horizontal_position
    global depth
    return horizontal_position * depth


def process_commands():
    pass # if "direction" in string, apply string[-1] to global variable


def mod_horizontal_position():
    pass


def mod_depth():
    pass


print(f'The product of horizontal position by final depth is {multiple_pos_by_depth()}.')
