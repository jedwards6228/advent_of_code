import re

input_file = 'test.txt'
calibration_document = [str(x.strip('\n')) for x in open(input_file).readlines()]


def calibration_values(line):
    num = int(str(re.findall("[0-9]", line)[0] + str(re.findall("[0-9]", line)[-1])))
    return num


def main():
    w_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    n_list_one = []
    n_list_two = []
    for line in calibration_document:
        n_list_one.append(calibration_values(line))
        for index, w in enumerate(w_list):
            #deal with situations where it has "twone"
            new_line = line.replace(w, str(index))
        n_list_two.append(calibration_values(new_line))

# use regex to replace


    return print(f"Part One: The sum of all calibration values is {sum(n_list_one)}.\n"
                 f"Part Two: The sum of all calibration values is {sum(n_list_two)}.")



if __name__ == "__main__":
    main()