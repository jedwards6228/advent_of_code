import operator

input_file = 'test.txt'
instruction_index_list = []
instruction_list = [str(x.strip('\n')) for x in open(input_file).readlines()]
operators = {
    "+": operator.add,
    "-": operator.sub,
}


def execute_instruction(i, acc):
    print(f'new i = {i} and index list = {instruction_index_list}')
    if i in instruction_index_list:
        print(f'acc is {acc} and we \'bout to end this motha fucka')
        return acc
    instruction_index_list.append(i)
    instruction = instruction_list[i]
    operation = instruction[:3]
    argument_sign = operators[instruction[4]]
    argument_number = int(instruction[5:])
    #print(f'{operation}, {argument_sign}, {argument_number}, {i}, {acc}')
    if operation == 'acc':
        return exec(run_acc(i, argument_sign, argument_number, acc))
    elif operation == 'jmp':
        return exec(run_jmp(i, argument_sign, argument_number, acc))
    elif operation == 'nop':
        return exec(run_nop(i, acc))
    else:
        return 'not working right now'


def run_acc(i, sign, number, acc):
    acc = sign(acc, number)
    i += 1
    return f'execute_instruction({i}, {acc})'


def run_jmp(i, sign, number, acc):
    i = sign(i, number)
    return f'execute_instruction({i}, {acc})'


def run_nop(i, acc):
    i += 1
    return f'execute_instruction({i}, {acc})'


print(f"The answer to part 1 is {execute_instruction(0, 0)}.")
