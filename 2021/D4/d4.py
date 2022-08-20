import re


def split_on_empty_lines(s):

    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())


input_file = "input.txt"
with open(input_file) as f:
    # read first line of the file as the draw list
    num_list = f.readline()
    num_list = num_list.strip('\n')
    num_list = num_list.split(',')
    # create bingo sheet
    all_bingo_boards = split_on_empty_lines(f.read())
drawn_num_list = []


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


def play_bingo(board_list):
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


def main():
    board_list = create_bingo_boards()
    # now just play bingo and if a board returns true, find out which one it is. somehow
    winner = play_bingo(board_list)
    score = board_list[winner].sum_unused_numbers(drawn_num_list) * int(drawn_num_list[-1])
    print(f'The final score of the winning board is {score}.')
    return


if __name__ == "__main__":
    main()


"""
Maybe using a class has fucked me over here as I don't know how to create multiple instances and operate them like this
"""