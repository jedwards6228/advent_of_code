input_file = 'input.txt'


def create_group_answer_list():
    group_answer_string = open(input_file).read()
    group_answer_list = group_answer_string.split('\n\n')
    return group_answer_list


def process_group_answers(answer_req):
    group_answer_list = create_group_answer_list()
    anyone_answer_count = 0
    everyone_answer_count = 0
    for group in group_answer_list:
        anyone_answer_set = set(str(x) for x in group.replace('\n',''))
        anyone_answer_count += len(anyone_answer_set)
        group = group.split('\n')
        group_string = ''.join(group)
        for x in group[0]:
            if group_string.count(x) == len(group):
                everyone_answer_count += 1
    if answer_req == "anyone":
        return anyone_answer_count
    if answer_req == "everyone":
        return everyone_answer_count


print(f'The number of times "ANYONE" answered "yes" is {process_group_answers("anyone")}.')
print(f'The number of times "EVERYONE" answered "yes" is {process_group_answers("everyone")}.')

#Need to make a string that has all elements of the group list