import operator

input_file = 'input.txt'
instruction_list = [str(x.strip('\n')) for x in open(input_file).readlines()]
operators = {
    "+": operator.add,
    "-": operator.sub,
}

index_dict = {
}


def execute_instruction(i, acc):
    instruction_index_list = []
    while i not in instruction_index_list:
        instruction_index_list.append(i)
        instruction = instruction_list[i]
        operation = instruction[:3]
        argument_sign = operators[instruction[4]]
        argument_number = int(instruction[5:])
        if operation == 'acc':
            i, acc = run_acc(i, argument_sign, argument_number, acc)
        elif operation == 'jmp':
            i, acc = run_jmp(i, argument_sign, argument_number, acc)
        elif operation == 'nop':
            i, acc = run_nop(i, acc)
    return acc


def fix_corrupt_instruction(i, acc):
    populate_index_dict()
    for index, inst in index_dict.items():
        change_inst(index)
        answer = test_instructions(i, acc)
        if answer:
            break
        change_inst(index)
    return answer


def change_inst(index):
    inst = instruction_list[index]
    operation = inst[:3]
    tag = inst[3:]
    if operation == 'jmp':
        instruction_list[index] = 'nop' + tag
        return
    elif operation == 'nop':
        instruction_list[index] = 'jmp' + tag
        return
    else:
        return


def test_instructions(i, acc):
    temp_index_list = []
    while i < len(instruction_list):
        if i in temp_index_list:
            break
        temp_index_list.append(i)
        instruction = instruction_list[i]
        operation = instruction[:3]
        argument_sign = operators[instruction[4]]
        argument_number = int(instruction[5:])
        if operation == 'acc':
            i, acc = run_acc(i, argument_sign, argument_number, acc)
        elif operation == 'jmp':
            i, acc = run_jmp(i, argument_sign, argument_number, acc)
        elif operation == 'nop':
            i, acc = run_nop(i, acc)
    if i == len(instruction_list):
        return acc
    elif i > len(instruction_list) or i < 0:
        return False
    else:
        return False


def populate_index_dict():
    for index, inst in enumerate(instruction_list):
        if str(inst[:3]) == 'jmp':
            index_dict.update({index: inst})
        elif inst[:3] == 'nop':
            index_dict.update({index: inst})
        else:
            continue
    return


def run_acc(i, sign, number, acc):
    acc = sign(acc, number)
    i += 1
    return i, acc


def run_jmp(i, sign, number, acc):
    i = sign(i, number)
    return i, acc


def run_nop(i, acc):
    i += 1
    return i, acc


print(f"The answer to part 1 is {execute_instruction(0, 0)}.")
print(f"The answer to part 2 is {fix_corrupt_instruction(0, 0)}.")
