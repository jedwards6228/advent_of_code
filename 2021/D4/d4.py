import re


def split_on_empty_lines(s):

    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())


input_file = "test.txt"
with open(input_file) as f:
    # read first line of the file as the draw list
    num_list = f.readline()
    num_list = num_list.strip('\n')
    num_list = num_list.split(',')
    # create bingo sheet
    all_bingo_boards = split_on_empty_lines(f.read())


class BingoBoard:
    def __init__(self, bingo_string):
        # create a matrix from the bingo string
        self.bingo_rows = [[int(num) for num in row.split()] for row in bingo_string.split("\n")]
        self.bingo_columns = [[row[i] for row in self.bingo_rows] for i in range(len(self.bingo_rows[0]))]
        self.bingo_diagonals = self.find_diagonals()
        self.win_conditions = self.bingo_diagonals + self.bingo_rows + self.bingo_columns

    def find_diagonals(self):
        i = 1
        l_to_r = []
        r_to_l = []
        while i - 1 < len(self.bingo_rows[0]):
            l_to_r.append(self.bingo_rows[i - 1][i - 1])
            r_to_l.append(self.bingo_rows[i - 1][-i])
            i += 1
        return [l_to_r, r_to_l]

    def check_bingo(self, drawn_num_list):
        for condition in self.win_conditions:
            for index, num in enumerate(condition):
                if num not in drawn_num_list:
                    break
                elif index + 1 == len(condition):
                    print('Bingo!')
                    return True
                else:
                    continue
        return False


def create_bingo_boards():
    board_id = 1
    for board in all_bingo_boards:
        create_board = f'bingo_board_{board_id} = BingoBoard(all_bingo_boards[0])'
        exec("bingo_board_1 = 'wow'")
        print(f'board {board_id} created')
        board_id += 1
    print(bingo_board_1)
    return


def main():
    create_bingo_boards()
    return


if __name__ == "__main__":
    main()


"""
Maybe using a class has fucked me over here as I don't know how to create multiple instances and operate them like this
"""