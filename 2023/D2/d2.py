from pathlib import Path


input_file = Path(__file__).with_name('test.txt')
input_list = [str(x.strip('\n')) for x in open(input_file).readlines()]


def part_one():
    return





def main():
    # call a function and pass in the cube limits in case p2 has new limits (seems likely)
    for line in input_list:
        # create an int representing the game number
        game = int(line[:line.find(':')].strip('Game '))
        # define where the cube info starts
        color_start = line.find(':') + 2
        # from color start, create a list for each set separated by '; '
        set_list = line[color_start:].split('; ')
        # separate each set into its own item and then split by ', '
        for cube_set in set_list:
            red = 0
            green = 0
            blue = 0
            cubes = cube_set.split(', ')
            # find the color and count separately for each set
            for color_count in cubes:
                count = int(color_count[:color_count.find(' ')])
                color = color_count[color_count.find(' ') + 1:]
                if color == 'red':
                    red += count
                elif color == 'green':
                    green += count
                elif color == 'blue':
                    blue += count
            print(red)            

        
        part_one_sum = part_one()

    
    return print(f'part 1 solution: {None}.\n'
                 f'part 2 solutin: {None}.')


if __name__ == '__main__':
    main()
