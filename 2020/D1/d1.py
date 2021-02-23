def create_input_object(input_file):
    input_numbers = tuple(int(x) for x in open(input_file).readlines())
    return input_numbers


def find_two_int(input_numbers):
    for index, k in enumerate(input_numbers):
        if index + 1 == len(input_numbers):
            print ("No Solution Found")
            break
        while index < len(input_numbers) - 1:
            int1 = k
            int2 = input_numbers[index + 1]
            if int1 + int2 == 2020:
                return int1, int2
            index += 1


def find_three_int(input_numbers):
    for index, k in enumerate(input_numbers):
        if index + 1 == len(input_numbers):
            print("No Solution Found")
            break
        int1 = k
        i2 = index + 1
        while i2 < len(input_numbers) - 2:
            i3 = i2 + 1
            int2 = input_numbers[i2]
            while i3 < len(input_numbers) - 1:
                int3 = input_numbers[i3]
                if int1 + int2 + int3 == 2020:
                    return int1, int2, int3
                i3 += 1
            i2 += 1


def multiply_two(input_file):
    input_numbers = create_input_object(input_file)
    int1, int2 = find_two_int(input_numbers)
    return int1 * int2


def multiply_three(input_file):
    input_numbers = create_input_object(input_file)
    int1, int2, int3 = find_three_int(input_numbers)
    return int1 * int2 * int3


#Part 1
print(f"The answer to part 1 is {multiply_two('input.txt')}")
#Part 2
print(f"The answer to part 2 is {multiply_three('input.txt')}")