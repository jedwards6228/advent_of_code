input_file = 'input.txt'
req_list = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
opt_list = ['cid:']


def create_passport_list():
    passport_string = open(input_file).read()
    passport_list = passport_string.split('\n\n')  #Creates a list split by each blank line
    return passport_list


def check_passport():
    passport_list = create_passport_list()
    valid_count = 0
    for passport in passport_list:
        req = True
        for req in req_list:
            if req not in passport:
                req = False
                break
        if req:
            valid_count += 1
    return valid_count


print(f"The number of valid passports is {check_passport()}")