input_file = 'input.txt'
row_range = range(0, 128)
col_range = range(0, 8)
seat_map = [[int(row * 8 + col) for col in col_range] for row in row_range]
seat_id_list = []

def create_instruction_list(file):
    bpass_list = open(file).readlines()
    return bpass_list


def calculate_highest_seat_id():
    boarding_pass_list = create_instruction_list(input_file)
    for boarding_pass in boarding_pass_list:
        print(boarding_pass)
        instruction_count = 0
        row_max = len(seat_map)
        row_min = 0
        col_max = len(seat_map[0])
        col_min = 0
        while instruction_count < len(boarding_pass):
            instruction = boarding_pass[instruction_count]
            if instruction == 'F':
                row_max -= (row_max - row_min) / 2
            elif instruction == 'B':
                row_min += (row_max - row_min) / 2
            elif instruction == 'R':
                col_max -= (col_max - col_min) / 2
            elif instruction == 'L':
                col_min += (col_max - col_min) / 2
            else:
                print('i dunno what just happened?!')
            instruction_count += 1
        seat_id_list.append(seat_map[row_min[col_min]])
        print(seat_id_list)
    return

calculate_highest_seat_id()
