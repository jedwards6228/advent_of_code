input_file = 'input.txt'
row_range = range(0, 128)
col_range = range(0, 8)
seat_map = [[int(row * 8 + col) for col in range(0, 8)] for row in range(0, 128)]


def create_instruction_list(file):
    bpass_list = open(file).readlines()
    return bpass_list


def calculate_highest_seat_id():
    boarding_pass_list = create_instruction_list(input_file)

