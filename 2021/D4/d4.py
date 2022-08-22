import re


def split_on_empty_lines(s):

    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())


class BingoBoard:
    def __init__(self, bingo_string):
        # create a matrix from the bingo string
        self.bingo_rows = [[int(num) for num in row.split()] for row in bingo_string.split("\n")]
        self.bingo_columns = [[row[i] for row in self.bingo_rows] for i in range(len(self.bingo_rows[0]))]
        self.bingo_diagonals = self.find_diagonals()
        self.win_conditions_no_diag = self.bingo_rows + self.bingo_columns
        # this next one is confusing
        self.num_list = [num for row in self.bingo_rows for num in row]

    def find_diagonals(self):
        i = 1
        l_to_r = []
        r_to_l = []
        while i - 1 < len(self.bingo_rows[0]):
            l_to_r.append(self.bingo_rows[i - 1][i - 1])
            r_to_l.append(self.bingo_rows[i - 1][-i])
            i += 1
        return [l_to_r, r_to_l]

    def check_bingo(self, draw_list):
        for condition in self.win_conditions_no_diag:
            for index, num in enumerate(condition):
                if num not in draw_list:
                    break
                elif index + 1 == len(condition):
                    return True
                else:
                    continue
        return False

    def sum_unused_numbers(self, draw_list):
        unused_list = []
        for num in self.num_list:
            if num not in draw_list:
                unused_list.append(num)
            else:
                continue
        return sum(unused_list)


def create_bingo_boards():
    # I think this is an anonymous list
    board_list = []
    for board in all_bingo_boards:
        # creates a bingo board with no variable name and stores it in an index in a list
        board_list.append(BingoBoard(board))
    return board_list


def play_bingo():
    drawn_num_list.clear()
    for num in num_list:
        drawn_num_list.append(int(num))
        for index, board in enumerate(board_list):
            check = board.check_bingo(drawn_num_list)
            if check:
                return index
            else:
                continue
    print('no bingo :(')
    return None


def find_score(board):
    return board_list[board].sum_unused_numbers(drawn_num_list) * int(drawn_num_list[-1])


def find_last_winner():
    """ +
    drawn_num_list = num_list.copy()
    popped_var = None
    for i in range(len(num_list)
    popped_var = drawn_num_list.pop()
    for board in list
    board.check_bingo(drawn_num_list)
    if board gets bingo: continue
    else: temp_num_list.append popped var

    """
    return


def main():
    first_winner = play_bingo()
    last_winner = find_last_winner()
    print(f'The final score of the first winner is {find_score(first_winner)}.')
    print(f'The final score for the last winner is {find_score(last_winner)}.')
    return


input_file = "test.txt"
with open(input_file) as f:
    # read first line of the file as the draw list
    num_list = f.readline()
    num_list = num_list.strip('\n')
    num_list = num_list.split(',')
    # create bingo sheet
    all_bingo_boards = split_on_empty_lines(f.read())
drawn_num_list = []
board_list = create_bingo_boards()


if __name__ == "__main__":
    main()


"""

"""