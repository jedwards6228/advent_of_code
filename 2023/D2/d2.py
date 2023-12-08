from pathlib import Path


input_file = Path(__file__).with_name('input.txt')
input_list = [str(x.strip('\n')) for x in open(input_file).readlines()]


def part_one():
    return


def main():
    # call a function and pass in the cube limits in case p2 has new limits (seems likely)
    for line in input_list:
        part_one_sum = part_one()

    
    return print(f'part 1 solution: {None}.\n'
                 f'part 2 solutin: {None}.')


if __name__ == '__main__':
    main()
