input_file = 'input.txt'
num_list = [int(x.strip('\n')) for x in open(input_file).readlines()]
current_num_list = num_list.copy()
run_length = 25
run_list = [int(current_num_list.pop(0)) for x in range(run_length)]
invalid_num = 0


def find_invalid_num():
    global invalid_num
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


def find_encryption_weakness():
    cont_list = find_contiguous_list()
    lowest_cont = min(cont_list)
    highest_cont = max(cont_list)
    encryption_weakness = lowest_cont + highest_cont
    return encryption_weakness


def find_contiguous_list():
    for index, num in enumerate(num_list):
        cont_list = []
        num_sum = 0
        i = 0
        while num_sum < invalid_num:
            num_sum += num_list[index + i]
            cont_list.append(num_list[index + i])
            i += 1
        if num_sum == invalid_num:
            return cont_list
        else:
            continue


print(f"The invalid number is {find_invalid_num()}.")
print(f"The encryption weakness is {find_encryption_weakness()}.")
