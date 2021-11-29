input_file = 'test.txt'
seat_layout = [[str(space) for space in row.strip('\n')] for row in open(input_file).readlines()]


def find_stable_seating_arrangement():
    global seat_layout
    occupied_seats = 0
    next_seat_layout = []
    while next_seat_layout != seat_layout:
        seat_layout = next_seat_layout.copy()
        seat_status_changer(seat_layout, next_seat_layout)
    for row in seat_layout:
        occupied_seats += row.count('#')
    return occupied_seats


# change each item in next_seat_layout
def seat_status_changer(current_layout, next_layout):
    for row in


def create_adjacent_seat_list(subject):
    pass


print(f"The number of occupied seats in a stable state is {find_stable_seating_arrangement()}.")

#