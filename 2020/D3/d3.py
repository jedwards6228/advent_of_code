# Look into numpy and matplotlib.  I should be able to do something like this:
#       Number of lines in input determines y.  multiply that times 3 to find how many x points will be needed
#       Count number of characters in each line.  Multiply that until x count is higher than required and no more
#       Apply that multiplier by appending copies of each line to themselves until they have that many characters
#       May want to do a matrix style list thing where there are lists in lists.  Unsure if that is easier than
#       making a single list with very long strings.  As I write it maybe long strings is the way so it's less difficult
#       to handle overflow from one repeated line to another.


def create_input_list(input_file):
    input_list = list(open('input_file').readlines())       # Create a list with each line
    for index, x in enumerate(input_list):      # Clean the \n out of every entry
        input_list[index] = x.strip('\n')