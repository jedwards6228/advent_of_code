import operator

input_file = 'input.txt'
instruction_index_list = []
instruction_list = [str(x.strip('\n')) for x in open(input_file).readlines()]
operators = {
    "+": operator.add,
    "-": operator.sub,
}


def execute_instruction(i, acc):
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
        else:
            return 'not working right now'
    return acc


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
