input_file = 'input.txt'
row_range = range(0, 128)
col_range = range(0, 8)
seat_map = [[int(row * 8 + col) for col in col_range] for row in row_range]
seat_id_list = []


def create_instruction_list():
    bpass_list = open(input_file).readlines()
    return bpass_list


def create_seat_id_list():
    boarding_pass_list = create_instruction_list()
    for boarding_pass in boarding_pass_list:
        instruction_count = 0
        row_max = len(seat_map)
        row_min = 0
        col_max = len(seat_map[0])
        col_min = 0
        while instruction_count < len(boarding_pass) - 1:
            instruction = boarding_pass[instruction_count]
            if instruction == 'F':
                row_max -= (row_max - row_min) / 2
            elif instruction == 'B':
                row_min += (row_max - row_min) / 2
            elif instruction == 'L':
                col_max -= (col_max - col_min) / 2
            elif instruction == 'R':
                col_min += (col_max - col_min) / 2
            else:
                print('i dunno what just happened?!')
            instruction_count += 1
        col_in_row = seat_map[int(row_min)]
        seat_id_list.append(col_in_row[int(col_min)])
    return seat_id_list


def find_missing_num():
    create_seat_id_list()
    for x in range(min(seat_id_list), max(seat_id_list)):
        if x not in seat_id_list:
            return x


print(f'The highest seat ID on a boarding pass is {max(create_seat_id_list())}.')
print(f'Your seat number is {find_missing_num()}.')
