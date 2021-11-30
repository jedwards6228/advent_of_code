input_file = 'test.txt'
seat_layout = [[str(space) for space in row.strip('\n')] for row in open(input_file).readlines()]
next_seat_layout = []


def find_stable_seating_arrangement():
    global seat_layout
    global next_seat_layout
    occupied_seats = 0
    while next_seat_layout != seat_layout:
        next_seat_layout = seat_layout.copy()
        seat_status_changer()
    for row in seat_layout:
        occupied_seats += row.count('#')
    return occupied_seats


# change each item in next_seat_layout
def seat_status_changer():
    global seat_layout
    global next_seat_layout
    for index_row, row in enumerate(seat_layout):
        new_row = row.copy()
        for index_seat, seat in enumerate(row):
            if seat == '.':
                continue
            adjacent_seat_list = create_adjacent_seat_list(index_row, index_seat)
            if seat == 'L' and '#' not in adjacent_seat_list:
                new_row[index_seat] = '#'
            elif seat == '#' and adjacent_seat_list.count('#') >= 4:
                new_row[index_seat] = 'L'
        next_seat_layout[index_row] = new_row
    return


def create_adjacent_seat_list(row, seat):
    print(row, seat)
    global seat_layout
    adjacent_seat_list = []
    for y in range(3):
        if row == 0 and y == 0:
            continue
        for x in range(3):
            if seat == 0 and x == 0:
                continue
            if y == 1 and x == 1:
                continue
            current_row = seat_layout[y - 1]
            adjacent_seat_list.append(current_row[x - 1])
    print(adjacent_seat_list)
    return adjacent_seat_list


print(f"The number of occupied seats in a stable state is {find_stable_seating_arrangement()}.")
