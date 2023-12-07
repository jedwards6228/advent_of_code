import re
from pathlib import Path

input_file = Path(__file__).with_name('input.txt')
calibration_document = [str(x.strip('\n')) for x in open(input_file).readlines()]


# return the first and last numeric value in a string
def calibration_values(line):
    num = int(re.findall('[0-9]', line)[0] + re.findall('[0-9]', line)[-1])
    return num


def main():
    word_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    part_one = 0
    part_two = 0
    for line in calibration_document:
        line_list = list(line)
        part_one += calibration_values(line)  # solve for part 1
        for character_index, character in enumerate(line_list):  # go through each character in the line
            for w_index, w in enumerate(word_list):  # check for each word
                temp_index = 0
                while w[temp_index] == line_list[character_index + temp_index] \
                        and character_index + len(w) <= len(line_list):  # verify a whole word exists
                    if temp_index == len(w) - 1:  # replace the first character of the word with the number
                        line_list[character_index] = str(w_index)
                        break
                    temp_index += 1
        part_two += calibration_values("".join(line_list))  # solve for part 2
    return print(f'Part One: The sum of all calibration values is {part_one}.\n'
                 f'Part Two: The sum of all calibration values is {part_two}.')


if __name__ == "__main__":
    main()
