from pathlib import Path
import re

# initial input parsing from a file with a dynamic path to the folder it's in
input_file = Path(__file__).with_name('input.txt')
input_list = [str(x.strip('\n')) for x in open(input_file).readlines()]

full_number_list = []


class Number:
    def __init__(self, digit, row, column):
        self.full_number = self.combine_digits(digit, row, column)
        self.row = row
        self.adjacent_symbols = self.find_adjacent_symbols(row, column, len(self.full_number))
        return  
    

    def combine_digits(self, digit, row, column):
        number_base = digit
        i = 1
        while input_list[row][min(len(input_list[row]) - 1, column + i)].isnumeric() and column + i < len(input_list[row]):
            number_base += input_list[row][column + i]
            i += 1
        return number_base
    
    
    def find_adjacent_symbols(self, row, column, num_length):
        current_symbol_list = []
        # prevent any rows and indexes that we look at from exceeding the length of their source
        first_row = max(0, row - 1)
        last_row = min(len(input_list), row + 2)
        first_index = max(0, column - 1)
        last_index = min(len(input_list[row]), column + num_length + 1)
        for x in range(first_row, last_row):
            for y in range(first_index, last_index):
                if is_symbol(input_list[x][y]):
                    current_symbol_list.append(input_list[x][y])
        return current_symbol_list
    

def check_number_list():
    for x in full_number_list:
        print(f'full number: {x.full_number}; adjacent symbols: {x.adjacent_symbols}')
    return


def is_symbol(character):
    if character.isnumeric() or character == '.':
        return False
    else: 
        return True 


def solve_part_one(): 
    total = 0
    for num in full_number_list:
        if len(num.adjacent_symbols) > 0:
            total += int(num.full_number)    
    return total


def main():
    part_two_sum = 0
    for row_number, row_content in enumerate(input_list):
        for column_number, character in enumerate(row_content):
            # no action if previous character was numeric, or if current character is a symbol or '.'
            if row_content[column_number - 1].isnumeric() or is_symbol(character) or character == '.':
                continue
            else:
                full_number_list.append(Number(character, row_number, column_number))
    part_one_sum = solve_part_one()
    # check_number_list()
    return print(f'The sum of the part numbers for part one is {part_one_sum} \n'
                 f'The sum of the gear ratios for part two is {part_two_sum}')


if __name__ == '__main__':
    main()
