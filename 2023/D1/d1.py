import re

input_file = 'input.txt'
calibration_document = [str(x.strip('\n')) for x in open(input_file).readlines()]


def calibration_values(line):
    num = int(re.findall("[0-9]", line)[0] + re.findall("[0-9]", line)[-1])
    return num


def main():
    word_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    part_one = 0
    part_two = 0
    for line in calibration_document:
        line_list = list(line)
        part_one += calibration_values(line)
        for character_index, character in enumerate(line_list):
            # print("character is " + character)
            for w_index, w in enumerate(word_list):
                temp_index = 0
                while w[temp_index] == line_list[character_index + temp_index] and character_index + len(w) <= len(line_list):
                    if temp_index == len(w) - 1:
                        line_list[character_index] = str(w_index)
                        break
                    temp_index += 1
        part_two += calibration_values("".join(line_list))
    return print(f"Part One: The sum of all calibration values is {part_one}.\n"
                 f"Part Two: The sum of all calibration values is {part_two}.")


if __name__ == "__main__":
    main()
