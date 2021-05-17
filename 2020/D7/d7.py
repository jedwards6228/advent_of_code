import re

input_file = 'test.txt'
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
        value_list = bag_dict[key]
        new_value_list = []
        for value in value_list:
            if value[0].isnumeric():
                multiplier = int(value[0])
                value = value.strip(f'{multiplier} ')
                for x in range(multiplier):
                    new_value_list.append(value)
            else:
                new_value_list.append(value)
        expanded_dict[key] = new_value_list
    return


create_bag_dict()
create_expanded_dict()
print(expanded_dict)



"""
test_dict = {
    'a': ['b', 'b', 'c'],
    'b': ['c', 'c'],
    'c': ['a']
}

This creates a dictionary where keys have 
lists as values and should work for 
creating a dictionary of bags and a list 
of the bags those contain

temp_list = test_dict['a']

would result in:
temp_list = ['b', 'b', 'c']

Must change bags to bag, remove "contains" and "contain", remove ',' and '.',
and remove leading/trailing spaces on the key/value before putting it into 
the dictionary
May need to remove an '' from the value as well
Used pop to get the key
"""
