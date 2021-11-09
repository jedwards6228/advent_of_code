import operator

input_file = 'test.txt'
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


#this needs to return the pt 2 answer
#this needs to count which instruction is changing
def fix_corrupt_instruction():
    populate_index_dict()
    for index, inst in index_dict:
        change_inst(index, inst)
        answer = test_instructions()
        if answer != False:
            break
        change_inst(index, inst) # this will change the instruction back
    return answer


#this will change an instruction from jmp to nop or the other way
def change_inst(index, inst):
    operation = inst[:3]
    tag = inst[3:]
    if operation == 'jmp':
        instruction_list[index] = 'nop' + tag
    elif operation == 'nop':
        instruction_list[index] = 'jmp' + tag
    else:
        print('something is wrong in change_inst')
    return


#this will be similar to the pt 1 code but try to find the result when executing inst at len(instruction_list) + 1
def test_instructions():
    pass


def populate_index_dict():
    for index, inst in enumerate(instruction_list):
        if inst == 'jmp' or 'nop':
            index_dict.update({index : inst})
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
print(f"The answer to part 2 is {}.")
