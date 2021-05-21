input_file = 'input.txt'
bag_dict = {}
expanded_dict = {}


# Creates a dictionary where bag color: list(# bag color)
def create_bag_dict():
    input_list = open(input_file).readlines()
    for line in input_list:
        line = line.strip('\n')
        line = line.replace('bags', 'bag')
        line = line.replace('contain ', '')
        line = line.replace('contains ', '')
        line = line.replace(',', '')
        line = line.replace('.', '')
        value_list = line.split(' bag')
        value_list.remove('')
        for index, x in enumerate(value_list):
            value_list[index] = x.strip()
        key = value_list.pop(0)
        bag_dict[key] = value_list
    return


def create_expanded_dict():
    for key in bag_dict.keys():
        value_list = bag_dict[key].copy()
        new_value_set = set()
        for value in value_list:
            if value[0].isnumeric():
                value = value.strip(f'{value[0]} ')
            new_value_set.add(value)
            if value == 'no other':
                continue
            for sub_value in bag_dict[value]:
                if sub_value == 'no other':
                    continue
                value_list.append(sub_value)
        expanded_dict[key] = new_value_set
    return


def count_bags_containing_target(target):
    count = 0
    for key in expanded_dict.keys():
        if target in expanded_dict[key]:
            count += 1
    return count


def count_bags_inside_target(target):
    count = 0
    value_list = bag_dict[target].copy()
    for value in value_list:
        if value == 'no other':
            continue
        elif value[0].isnumeric():
            multiplier = int(value[0])
            for i in range(0, multiplier):
                if bag_dict[value.strip(f'{value[0]} ')] == 'no other':
                    break
                for sub_value in bag_dict[value.strip(f'{value[0]} ')]:
                    if sub_value == 'no other':
                        break
                    value_list.append(sub_value)
            count = count + multiplier
        else:
            print('something wrong?')
    return count


create_bag_dict()
create_expanded_dict()


print(f"The number of bag colors that can contain at least one "
      f"shiny gold bag is {count_bags_containing_target('shiny gold')} ")
print(f"The number of bags inside of a single shiny gold bag is {count_bags_inside_target('shiny gold')}")
