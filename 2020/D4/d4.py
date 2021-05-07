import re

input_file = 'test.txt'
req_list = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
opt_list = ['cid:']
field_dict = {
    "byr:": "validate_byr(input)",
    "iyr:": "validate_iyr(input)",
    "eyr:": "validate_eyr(input)",
    "hgt:": "validate_hgt(input)",
    "hcl:": "validate_hcl(input)",
    "ecl:": "validate_ecl(input)",
    "pid:": "validate_pid(input)",
    "cid:": "validate_cid(input)"
}


def create_passport_list():
    passport_string = open(input_file).read()
    passport_list = passport_string.split('\n\n')  # Creates a list split by each blank line
    return passport_list


def check_passport(part):
    passport_list = create_passport_list()
    valid_req_count = 0
    valid_passport_count = 0
    passport_itter = 0      # for testing
    for passport in passport_list:
        passport_itter += 1      # for testing
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
                input = field.replace(code, '')
                status = exec(field_dict[code])
                if status == 'valid':
                    valid_passport_count += 1
                    print(f'{code} is valid on passport {passport_itter}')      # for testing
                if status == 'unknown':
                    print(f'{code} is unknown on passport {passport_itter}')      # for testing
                if status == 'invalid':
                    print(f'{code} is invalid on passport {passport_itter}')      # for testing
                    break
    if part == 1:
        return valid_req_count
    if part == 2:
        return valid_passport_count


# byr = 4 digits; low = 1920; high = 2002
def validate_byr(input):
    status = 'unknown'
    if 1920 <= int(input) <= 2002:
        status = 'valid'
    if 1920 > int(input) > 2002:
        status = 'invalid'
    if len(input) != 4:
        status = 'invalid'
    return status


# iyr = 4 digits; low = 2010; high = 2020
def validate_iyr(input):
    status = 'unknown'
    if 2010 <= int(input) <= 2020:
        status = 'valid'
    if 2010 > int(input) > 2020:
        status = 'invalid'
    if len(input) != 4:
        status = 'invalid'
    return status


# eyr = 4 digits; low = 2020; high = 2030
def validate_eyr(input):
    status = 'unknown'
    if 2020 <= int(input) <= 2030:
        status = 'valid'
    if 2020 > int(input) > 2030:
        status = 'invalid'
    if len(input) != 4:
        status = 'invalid'
    return status


# hgt = a number followed by "cm" or "in"
#       if cm: low = 150; high = 193
#       if in: low = 59; high = 76
def validate_hgt(input):
    method = input[-2] + input[-1]
    mod_input = input.replace(method, '')
    status = 'unknown'
    if method == 'cm' and 150 <= int(mod_input) <= 193:
        status = 'valid'
    if method == 'in' and 59 <= int(mod_input) <= 76:
        status = 'valid'
    if method == 'cm' and 150 > int(mod_input) > 193:
        status = 'invalid'
    if method == 'in' and 59 > int(mod_input) > 76:
        status = 'invalid'
    if method != 'in' or method != 'cm':
        status = 'invalid'
    return status


# hcl = a "#" followed by 6 characters (0-9 or a-f)
def validate_hcl(input):
    status = 'unknown'
    if re.search('#[0-9a-f]{6}', input):
        status = 'valid'
    if not re.search('#[0-9a-f]{6}', input):
        status = 'invalid'
    return status


# ecl = exactly one of: "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
def validate_ecl(input):
    ecl_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    status = 'unknown'
    if input in ecl_list:
        status = 'valid'
    if input not in ecl_list:
        status = 'invalid'
    return status


# pid = a nine-digit number including zeroes
def validate_pid(input):
    status = 'unknown'
    if input.isnumeric():
        status = 'valid'
    if len(input) != 9:
        status = 'invalid'
    return status


# cid = ignore
def validate_cid(input):
    status = 'valid'
    return status


print(f"Part 1: The number of passports that have all requirements is {check_passport(1)}")
print(f"Part 2: The number valid passports is {check_passport(2)}")
