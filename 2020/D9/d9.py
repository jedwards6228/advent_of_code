

input_file = 'test.txt'
num_list = [int(x.strip('\n')) for x in open(input_file).readlines()]
current_num_list = num_list.copy()
run_length = 5
run_list = [int(current_num_list.pop(0)) for x in range(run_length)]


def find_invalid_num():
    for x in range(len(current_num_list)):
        invalid_num = current_num_list[0]
        valid = validate_next_num(invalid_num)
        if valid:
            rotate_num()
            continue
        else:
            return invalid_num


def validate_next_num(next_num):
    for item in run_list:
        if next_num - item in run_list:
            return True
        else:
            continue
    return False


def rotate_num():
    run_list.pop(0)
    run_list.append(current_num_list.pop(0))
    return


# part 2
def find_encryption_weakness():
    pass


print(f"The invalid number is {find_invalid_num()}.")
print(f"The encryption weakness is {find_encryption_weakness()}.")
