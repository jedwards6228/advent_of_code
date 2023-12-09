from pathlib import Path

# initial input parsing from a file with a dynamic path to the folder it's in
input_file = Path(__file__).with_name('input.txt')
input_list = [str(x.strip('\n')) for x in open(input_file).readlines()]

# global dictionaries for logging each part's relevant data
part_one_log = {}
part_two_log = {}


def part_one_eval(game, color_dict):
    red_limit = 12
    green_limit = 13
    blue_limit = 14
    # log game as fasle if it exceeds the set limits
    if color_dict['red'] > red_limit or color_dict['green'] > green_limit or color_dict['blue'] > blue_limit:
        part_one_log[game] = False
    return


def part_two_eval(game, color_dict):
    # If the log has a color value lower than the one being passed, replace it with the higher value
    for color in color_dict:
        if color_dict[color] > part_two_log[game][color]:
            part_two_log[game][color] = color_dict[color]
    return 


def sum_game_id(game_log):
    sum = 0
    for game in game_log:
        if game_log[game]:
            sum += game
    return sum
    

def sum_powers(game_log):
    total_power = 0
    for game in game_log:
        power = 1
        for color in game_log[game]:
            power *= game_log[game][color]
        total_power += power
    return total_power


def main():
    for line in input_list:
        # create an int representing the game number
        game = int(line[:line.find(':')].strip('Game '))
        # log the game in each part's dictionary
        part_one_log[game] = True
        part_two_log[game] = {'red': 0, 'green': 0, 'blue': 0}
        # define where the cube info starts
        color_start = line.find(':') + 2
        # from color start, create a list for each set separated by '; '
        set_list = line[color_start:].split('; ')
        # separate each set into its own item and then split by ', '
        for cube_set in set_list:
            color_dict = {
                'red': 0,
                'green': 0,
                'blue': 0
            }
            cubes = cube_set.split(', ')
            # find the color and count separately for each set
            for color_count in cubes:
                count = int(color_count[:color_count.find(' ')])
                color = color_count[color_count.find(' ') + 1:]
                color_dict[color] = count
            part_one_eval(game, color_dict)
            part_two_eval(game, color_dict)
    part_one_sum = sum_game_id(part_one_log)
    part_two_sum = sum_powers(part_two_log)
    return print(f'part 1 solution: {part_one_sum}.\n'
                 f'part 2 solutin: {part_two_sum}.')


if __name__ == '__main__':
    main()
