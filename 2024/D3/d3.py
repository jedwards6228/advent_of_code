import re
from pathlib import Path

# Get input file
input_file = Path(__file__).with_name('input.txt')

# Get corrupted instructions for later parsing
with open(input_file, 'r') as file:
    corrupted_instructions = file.read()


def handle_instructions(instruction_input):
    # Parse instructions
    parsed_instructions = [x.strip('mul\()').split(',') for x in re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', instruction_input)]
    # Convert instructions to ints
    instructions = [list(map(int, sublist)) for sublist in parsed_instructions]
    total = 0 
    for mul_set in instructions:
        total += mul_set[0] * mul_set[-1]
    return total


def part_two(): 
    # Remove all instructions between "don't()" and "do()" or the end of the input
    do_string = re.sub(r"don't\(\)((?:[^d]|d(?!o\(\)))*)(do\(\)?)", '', corrupted_instructions, flags=re.DOTALL)    
    return handle_instructions(do_string)


def main():
    print(f'The answer to part one is {handle_instructions(corrupted_instructions)}.')
    print(f'The answer to part two is {part_two()}.')
    return


if __name__ == '__main__':
    main()
