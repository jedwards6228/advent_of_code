import re

input_file = 'test.txt'
bag_dict = {}
expanded_dict = {}

def create_bag_dict():
    input_list = open(input_file).readlines()
    for line in input_list:




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

Must change bags to bag, remove "contain" and "contain", remove ',' and '.',
and remove leading/trailing spaces on the key/value before putting it into 
the dictionary
May need to remove an '' from the value as well
Used pop to get the key
"""
