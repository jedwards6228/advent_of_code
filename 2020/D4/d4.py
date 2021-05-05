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
    "pid:": "validate_pid(input)",
    "cid:": "validate_cid(input)"
}


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
# rewrite
def check_passport():
    passport_list = create_passport_list()
    for passport in passport_list:
        passport = passport.replace(' ', '\n')
        field_list = passport.split('\n')
        for field in field_list:
            code = str(field[0] + field[1] + field[2] + field[3])
            input = field.replace(code, '')
            exec(field_dict[code])  # <<<<< CURRENTLY TRYING TO EXECUTE A FUNC FROM A DICT AND PASS THE INPUT INTO IT

    pass


print(f"The number of valid passports is {check_passport()}")



# function to count characters for individual rules
def count_characters(input):
    return len(input)


# byr = 4 digits; low = 1920; high = 2002
def validate_byr(input):
    pass


# iyr = 4 digits; low = 2010; high = 2020
def validate_iyr(input):
    pass


# eyr = 4 digits; low = 2020; high = 2030
def validate_eyr(input):
    pass


# hgt = a number followed by "cm" or "in"
#       if cm: low = 150; high = 193
#       if in: low = 59; high = 76
def validate_hgt(input):
    pass


# hcl = a "#" followed by 6 characters (0-9 or a-f)
def validate_hcl(input):
    pass


# ecl = exactly one of: "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
def validate_ecl(input):
    pass


# pid = a nine-digit number including zeroes
def validate_pid(input):
    pass


# cid = ignore
def validate_cid(input):
    pass

