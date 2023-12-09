from pathlib import Path
import re

# initial input parsing from a file with a dynamic path to the folder it's in
input_file = Path(__file__).with_name('test.txt')
input_list = [str(x.strip('\n')) for x in open(input_file).readlines()]

number_positions = []

def main():
    for line in input_list:
        for number in re.findall('[0-9]+', line):
            pass
    return


if __name__ == '__main__':
    main()

"""
Need to find a number, then get the length of that number and the position of the first digit. 
Using those two elements, find all the "adjacent" tiles and if one of them has a symbol (non digit, 
non '.' character).

It might be good to only find the position of numbers and maybe the position of symbols in the 
main function. Determining if something is adjacent may be specific to part one, and should be 
part of its own function for now.

I might want to make a class for numbers that are found so I can assign multiple properties to them,
such as its position, the position of adjacent symbols, which symbols are adjacent, etc.
"""
