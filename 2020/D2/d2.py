import re


def create_input(input_file):  # Open input file as variable
    input_list = (open(input_file).readlines())
    return input_list


def parse_line(line):  # Parse individual lines into reps, topic, password
    parse_list = re.split(" ", line)
    rep_range = parse_list[0]
    topic = re.sub(":", "", parse_list[1])
    pw = re.sub("\n", "", parse_list[2])
    return str(rep_range), str(topic), str(pw)


def check_rules(input_string, part):  # Compare rules to password
    rep_range, topic, pw = parse_line(input_string)
    counter = int(pw.count(topic))  # Count the topic in the pw
    reps = re.split("-", rep_range)  # Split rep_range into a list with upper and lower
    reps = list(int(x) for x in reps)
    if reps[0] <= counter <= reps[-1] and part == 'p1':  # Validate counter
        return True
    if part == 'p2':
        return part_two_rules(reps, topic, pw)
    else:
        return False


def minus_one(a):  # Used to correct reps in part_two_rules()
    a -= 1
    return a


def part_two_rules(reps, topic, pw):
    reps = list(minus_one(x) for x in reps)
    if pw[reps[0]] == topic == pw[reps[-1]]:
        return False
    elif pw[reps[0]] == topic or pw[reps[-1]] == topic:
        return True


def valid_count(input_file, part):  # Count valid passwords
    valid_pw = 0
    input_list = create_input(input_file)
    for x in input_list:
        if check_rules(x, part):
            valid_pw += 1

    return valid_pw


# Print answers
print(f"There are {valid_count('input.txt', 'p1')} valid passwords for part 1")
print(f"There are {valid_count('input.txt', 'p2')} valid passwords for part 2")
