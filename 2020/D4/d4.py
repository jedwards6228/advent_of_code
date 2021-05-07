import re

input_file = 'input.txt'
req_list = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
opt_list = ['cid:']
field_dict = {
    "byr:": "validate_byr(input)",
    "iyr:": "validate_iyr(input)",
    "eyr:": "validate_eyr(input)",
    "hgt:": "validate_hgt(input)",
    "hcl:": "validate_hcl(input)",
    "ecl:": "validate_ecl(input)",
    "pid:": "validate_pid(input)"}


def create_passport_list():
    passport_string = open(input_file).read()
    passport_list = passport_string.split('\n\n')
    return passport_list


# byr = 4 digits; low = 1920; high = 2002
def validate_byr(input):
    global status
    status = 'unknown'
    if 1920 <= int(input) <= 2002:
        status = 'valid'
    else:
        status = 'invalid'
    if len(input) != 4:
        status = 'invalid'


# iyr = 4 digits; low = 2010; high = 2020
def validate_iyr(input):
    global status
    status = 'unknown'
    if 2010 <= int(input) <= 2020:
        status = 'valid'
    else:
        status = 'invalid'
    if len(input) != 4:
        status = 'invalid'


# eyr = 4 digits; low = 2020; high = 2030
def validate_eyr(input):
    global status
    status = 'unknown'
    if 2020 <= int(input) <= 2030:
        status = 'valid'
    else:
        status = 'invalid'
    if len(input) != 4:
        status = 'invalid'


# hgt = a number followed by "cm" or "in"
#       if cm: low = 150; high = 193
#       if in: low = 59; high = 76
def validate_hgt(input):
    global status
    method = input[-2] + input[-1]
    mod_input = input.replace(method, '')
    status = 'unknown'
    if method == 'cm':
        if 150 <= int(mod_input) <= 193:
            status = 'valid'
        else:
            status = 'invalid'
    elif method == 'in':
        if method == 'in' and 59 <= int(mod_input) <= 76:
            status = 'valid'
        else:
            status = 'invalid'
    else:
        status = 'invalid'


# hcl = a "#" followed by 6 characters (0-9 or a-f)
def validate_hcl(input):
    global status
    status = 'unknown'
    if re.search('#[0-9a-f]{6}', input):
        status = 'valid'
    else:
        status = 'invalid'


# ecl = exactly one of: "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
def validate_ecl(input):
    global status
    ecl_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    status = 'unknown'
    if input in ecl_list:
        status = 'valid'
    else:
        status = 'invalid'


# pid = a nine-digit number including zeroes
def validate_pid(input):
    global status
    status = 'unknown'
    if input.isnumeric():
        status = 'valid'
    if len(input) != 9:
        status = 'invalid'


def check_passport(part):
    passport_list = create_passport_list()
    valid_req_count = 0
    valid_passport_count = 0
    for passport in passport_list:
        valid_field_count = 0
        all_req = True
        for req in req_list:
            if req not in passport:
                all_req = False
                break
        if all_req:
            valid_req_count += 1
            passport = passport.replace(' ', '\n')
            field_list = passport.split('\n')
            for field in field_list:
                if not re.search('[a-z]{3}:', field):
                    break
                code = str(field[0] + field[1] + field[2] + field[3])
                if code == 'cid:':
                    continue
                input = field.replace(code, '')
                exec(field_dict[code])
                if status == 'valid':
                    valid_field_count += 1
                    if valid_field_count == 7:
                        valid_passport_count += 1
                if status == 'unknown':
                    print(f'{code} is an unknown code')
                if status == 'invalid':
                    break
    if part == 1:
        return valid_req_count
    if part == 2:
        return valid_passport_count


print(f"Part 1: The number of passports that have all requirements is {check_passport(1)}")
print(f"Part 2: The number valid passports is {check_passport(2)}")
